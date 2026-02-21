"""
Statuspage.io Parser

Parses RSS/Atom feeds and JSON API responses from Statuspage.io
(Used by OpenAI, GitHub, Stripe, Cloudflare, etc.)
"""

import re
import json
from typing import List, Dict, Any, Optional
import feedparser


def extract_severity(text: str) -> str:
    """Extract severity/impact from text."""
    text_lower = text.lower()

    if any(word in text_lower for word in ["critical", "outage", "down"]):
        return "critical"
    elif any(word in text_lower for word in ["major", "significant", "severe"]):
        return "major"
    elif any(word in text_lower for word in ["minor", "degraded", "partial"]):
        return "minor"
    elif any(word in text_lower for word in ["maintenance", "scheduled"]):
        return "maintenance"
    else:
        return "minor"


def extract_status(text: str) -> str:
    """Extract status from text."""
    text_lower = text.lower()

    if "resolved" in text_lower:
        return "resolved"
    elif "monitoring" in text_lower:
        return "monitoring"
    elif "identified" in text_lower:
        return "identified"
    elif "investigating" in text_lower:
        return "investigating"
    elif "update" in text_lower:
        return "update"
    else:
        return "investigating"


def extract_components_from_text(text: str) -> List[str]:
    """Try to extract component names from text."""
    components = []

    # Common patterns in status updates
    patterns = [
        r"(?:affecting|impacting|impact on)\s+([^.]+)",
        r"([A-Z][a-zA-Z\s]+(?:API|Service|Platform))",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        components.extend(matches)

    # Clean up and dedupe
    cleaned = []
    for comp in components:
        comp = comp.strip().strip(".")
        if comp and len(comp) > 2 and comp not in cleaned:
            cleaned.append(comp)

    return cleaned[:5]  # Limit to 5 components


def parse_rss_feed(xml_body: str) -> List[Dict[str, Any]]:
    """
    Parse RSS/Atom feed from Statuspage.io.

    Args:
        xml_body: Raw XML content

    Returns:
        List of parsed entries with id, title, message, status, severity, components
    """
    feed = feedparser.parse(xml_body)
    entries = []

    for entry in feed.entries:
        # Get the entry ID (unique identifier)
        entry_id = getattr(entry, "id", None) or getattr(entry, "link", str(hash(entry.title)))

        # Get title and summary
        title = getattr(entry, "title", "Unknown Incident")
        summary = getattr(entry, "summary", "") or getattr(entry, "description", "")

        # Clean HTML from summary
        summary_clean = re.sub(r"<[^>]+>", "", summary).strip()
        summary_clean = re.sub(r"\s+", " ", summary_clean)

        # Extract components from title or summary
        components = extract_components_from_text(f"{title} {summary_clean}")
        if not components:
            components = ["Service"]

        entries.append({
            "id": entry_id,
            "title": title,
            "message": summary_clean or title,
            "status": extract_status(title),
            "severity": extract_severity(f"{title} {summary_clean}"),
            "components": components,
            "published": getattr(entry, "published", None),
            "updated": getattr(entry, "updated", None),
        })

    return entries


def parse_json_api(body: str, provider_name: str) -> List[Dict[str, Any]]:
    """
    Parse JSON API response from Statuspage.io.

    Args:
        body: Raw JSON response
        provider_name: Name of the provider

    Returns:
        List of parsed incidents
    """
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return []

    incidents_data = data.get("incidents", [])
    parsed_incidents = []

    for incident in incidents_data:
        incident_id = incident.get("id", "")

        # Get components
        components = []
        for comp in incident.get("components", []):
            comp_name = comp.get("name", "")
            if comp_name:
                components.append(comp_name)

        if not components:
            components = ["Service"]

        # Get latest update
        updates = incident.get("incident_updates", [])
        latest_message = ""
        if updates:
            latest_message = updates[0].get("body", "")

        # Clean HTML
        latest_message = re.sub(r"<[^>]+>", "", latest_message).strip()

        parsed_incidents.append({
            "id": incident_id,
            "title": incident.get("name", "Unknown Incident"),
            "message": latest_message or incident.get("name", ""),
            "status": incident.get("status", "investigating"),
            "severity": incident.get("impact", "minor"),
            "components": components,
            "created_at": incident.get("created_at"),
            "updated_at": incident.get("updated_at"),
        })

    return parsed_incidents
