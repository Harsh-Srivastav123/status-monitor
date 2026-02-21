"""
In-Memory State Management

Stores all runtime state for monitors:
- ETags and Last-Modified headers for RSS monitors
- Content hashes for hash-based monitors
- Seen entry IDs to detect new incidents
- Detected incidents for API/UI
"""

from dataclasses import dataclass, field
from typing import Dict, Set, List, Any


@dataclass
class AppState:
    """Central state container for the application."""

    # RSS + ETag monitor state
    etags: Dict[str, str] = field(default_factory=dict)
    # { "OpenAI": "abc123etag" }

    last_modified: Dict[str, str] = field(default_factory=dict)
    # { "OpenAI": "Tue, 22 Feb 2026 10:00:00 GMT" }

    seen_entry_ids: Dict[str, Set[str]] = field(default_factory=dict)
    # { "OpenAI": {"entry_id_1", "entry_id_2"} }

    # Hash monitor state
    last_hashes: Dict[str, str] = field(default_factory=dict)
    # { "AWS": "sha256:abc123..." }

    seen_incident_ids: Dict[str, Set[str]] = field(default_factory=dict)
    # { "Render": {"incident_id_1", "incident_id_2"} }

    # Shared incident storage
    incidents: List[Dict[str, Any]] = field(default_factory=list)
    # Capped at 100 most recent

    # Monitor status tracking
    monitor_status: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    # { "OpenAI": {"status": "running", "last_check": "...", "checks": 5} }


# Global singleton instance
state = AppState()
