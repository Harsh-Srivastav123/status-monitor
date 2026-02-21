"""
RSS + ETag Monitor

Efficient monitoring using HTTP conditional requests.
When content hasn't changed, server returns 304 with empty body.
"""

import asyncio
from datetime import datetime
from typing import Dict, Any
import aiohttp

from core.state import state
from core.handler import on_change
from parsers.statuspage import parse_rss_feed


async def rss_monitor(provider: Dict[str, Any]) -> None:
    """
    Monitor a provider's RSS feed using ETag for efficiency.

    Args:
        provider: Provider config dict with name, rss_url, poll_interval
    """
    name = provider["name"]
    rss_url = provider["rss_url"]
    poll_interval = provider.get("poll_interval", 60)

    # Initialize monitor status
    state.monitor_status[name] = {
        "mode": "rss",
        "status": "starting",
        "last_check": None,
        "checks": 0,
        "changes_detected": 0,
        "url": rss_url
    }

    print(f"[MONITOR] Starting RSS monitor for {name}")

    # Track if this is the first run (baseline)
    first_run = True

    while True:
        headers = {}

        # Add conditional headers if we have them
        if name in state.etags:
            headers["If-None-Match"] = state.etags[name]
        if name in state.last_modified:
            headers["If-Modified-Since"] = state.last_modified[name]

        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(rss_url, headers=headers) as response:
                    state.monitor_status[name]["last_check"] = datetime.now().isoformat()
                    state.monitor_status[name]["checks"] += 1
                    state.monitor_status[name]["status"] = "running"

                    # 304 Not Modified - nothing changed
                    if response.status == 304:
                        pass  # Silent, efficient - no work needed

                    # 200 OK - content changed or first fetch
                    elif response.status == 200:
                        # Save ETag and Last-Modified for next request
                        if "ETag" in response.headers:
                            state.etags[name] = response.headers["ETag"]
                        if "Last-Modified" in response.headers:
                            state.last_modified[name] = response.headers["Last-Modified"]

                        # Parse the feed
                        body = await response.text()
                        entries = parse_rss_feed(body)

                        # Initialize seen set for this provider
                        if name not in state.seen_entry_ids:
                            state.seen_entry_ids[name] = set()

                        # Check each entry
                        for entry in entries:
                            entry_id = entry["id"]

                            # Skip if we've seen this entry
                            if entry_id in state.seen_entry_ids[name]:
                                continue

                            # Mark as seen
                            state.seen_entry_ids[name].add(entry_id)

                            # On first run, just build baseline (don't fire events)
                            if first_run:
                                continue

                            # Fire event for new entry
                            state.monitor_status[name]["changes_detected"] += 1
                            await on_change(
                                provider_name=name,
                                components=entry["components"],
                                message=entry["message"],
                                status=entry["status"],
                                severity=entry["severity"],
                                incident_id=entry_id,
                                title=entry["title"]
                            )

                        first_run = False

                    else:
                        print(f"[WARN] {name}: Unexpected status {response.status}")

        except asyncio.CancelledError:
            print(f"[MONITOR] Stopping RSS monitor for {name}")
            state.monitor_status[name]["status"] = "stopped"
            raise
        except Exception as e:
            state.monitor_status[name]["status"] = "error"
            state.monitor_status[name]["last_error"] = str(e)
            print(f"[ERROR] {name}: {e}")

        # Wait before next check
        await asyncio.sleep(poll_interval)
