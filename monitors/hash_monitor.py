"""
Hash-Based Polling Monitor

Fallback for providers without RSS feeds.
Uses SHA256 hash to detect changes in API response.
"""

import asyncio
import hashlib
from datetime import datetime
from typing import Dict, Any
import aiohttp

from core.state import state
from core.handler import on_change
from parsers.statuspage import parse_json_api


async def hash_monitor(provider: Dict[str, Any]) -> None:
    """
    Monitor a provider's API using hash-based change detection.

    Args:
        provider: Provider config dict with name, api_url, poll_interval
    """
    name = provider["name"]
    api_url = provider["api_url"]
    poll_interval = provider.get("poll_interval", 60)

    # Initialize monitor status
    state.monitor_status[name] = {
        "mode": "hash",
        "status": "starting",
        "last_check": None,
        "checks": 0,
        "changes_detected": 0,
        "url": api_url
    }

    print(f"[MONITOR] Starting hash monitor for {name}")

    # Track if this is the first run (baseline)
    first_run = True

    while True:
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(api_url) as response:
                    state.monitor_status[name]["last_check"] = datetime.now().isoformat()
                    state.monitor_status[name]["checks"] += 1
                    state.monitor_status[name]["status"] = "running"

                    if response.status == 200:
                        body = await response.text()

                        # Calculate hash of response body
                        current_hash = hashlib.sha256(body.encode()).hexdigest()
                        last_hash = state.last_hashes.get(name)

                        # First run - just save hash
                        if last_hash is None:
                            state.last_hashes[name] = current_hash
                            # Parse to build baseline of seen incidents
                            incidents = parse_json_api(body, name)
                            state.seen_incident_ids[name] = {
                                inc["id"] for inc in incidents if inc.get("id")
                            }
                            first_run = False

                        # Hash changed - something updated
                        elif current_hash != last_hash:
                            state.last_hashes[name] = current_hash

                            # Parse to find what changed
                            incidents = parse_json_api(body, name)

                            # Initialize seen set if needed
                            if name not in state.seen_incident_ids:
                                state.seen_incident_ids[name] = set()

                            for incident in incidents:
                                incident_id = incident.get("id", "")

                                # Skip if we've seen this incident
                                if incident_id in state.seen_incident_ids[name]:
                                    continue

                                # Mark as seen
                                if incident_id:
                                    state.seen_incident_ids[name].add(incident_id)

                                # Fire event
                                state.monitor_status[name]["changes_detected"] += 1
                                await on_change(
                                    provider_name=name,
                                    components=incident["components"],
                                    message=incident["message"],
                                    status=incident["status"],
                                    severity=incident["severity"],
                                    incident_id=incident_id,
                                    title=incident["title"],
                                    link=incident.get("link", ""),
                                    raw_payload=incident.get("raw_payload", {})
                                )
                    else:
                        print(f"[WARN] {name}: Status {response.status}")

        except asyncio.CancelledError:
            print(f"[MONITOR] Stopping hash monitor for {name}")
            state.monitor_status[name]["status"] = "stopped"
            raise
        except Exception as e:
            state.monitor_status[name]["status"] = "error"
            state.monitor_status[name]["last_error"] = str(e)
            print(f"[ERROR] {name}: {e}")

        # Wait before next check
        await asyncio.sleep(poll_interval)
