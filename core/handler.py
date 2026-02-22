"""
Event Handler

Called by monitors when a change is detected.
Handles:
1. Console output (assignment requirement)
2. In-memory storage for API
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from .state import state


async def on_change(
    provider_name: str,
    components: List[str],
    message: str,
    status: str,
    severity: str,
    incident_id: Optional[str] = None,
    title: Optional[str] = None,
    link: Optional[str] = None,
    raw_payload: Optional[Dict[str, Any]] = None
) -> None:
    """
    Handle detected incident/update.

    Args:
        provider_name: Name of the provider (e.g., "OpenAI")
        components: List of affected components/products
        message: Status message or update text
        status: Current status (investigating, resolved, etc.)
        severity: Impact level (minor, major, critical)
        incident_id: Unique incident identifier
        title: Incident title
        link: Link to incident page
        raw_payload: Raw data from provider for display
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # ============================================================
    # Step 1: Console Output (Assignment Requirement)
    # Format matches the example in assignment
    # ============================================================

    components_str = ", ".join(components) if components else "Unknown"

    print(f"\n[{timestamp}] Product: {provider_name} - {components_str}")
    print(f"Status: {message[:200]}{'...' if len(message) > 200 else ''}")
    if title:
        print(f"Incident: {title}")
    print(f"Severity: {severity.upper()}")
    print("─" * 60)

    # ============================================================
    # Step 2: Build incident record
    # ============================================================

    incident = {
        "id": incident_id or f"{provider_name}-{now.timestamp()}",
        "provider": provider_name,
        "components": components,
        "title": title or f"{status} - {components_str}",
        "message": message,
        "status": status,
        "severity": severity,
        "link": link or "",
        "detected_at": now.isoformat(),
        "timestamp": timestamp,
        "raw_payload": raw_payload or {}
    }

    # ============================================================
    # Step 3: Store in memory (newest first, cap at 100)
    # ============================================================

    state.incidents.insert(0, incident)
    if len(state.incidents) > 100:
        state.incidents.pop()
