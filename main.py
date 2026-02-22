"""
Status Monitor - Main Application

FastAPI app that:
1. Starts RSS and Hash monitors for all providers on startup
2. Serves a simple UI showing incidents and provider status
3. Provides REST API for incidents data
"""

import asyncio
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import PROVIDERS
from monitors.rss_monitor import rss_monitor
from monitors.hash_monitor import hash_monitor
from core.state import state


# Setup templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# Track background tasks and app start time
background_tasks = []
app_start_time_utc = None
app_start_time_ist = None

# IST timezone (UTC+5:30)
IST = timezone(timedelta(hours=5, minutes=30))


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager - runs on startup/shutdown.
    Starts all monitors as background tasks.
    """
    global background_tasks, app_start_time_utc, app_start_time_ist

    # Record application start time
    app_start_time_utc = datetime.now(timezone.utc)
    app_start_time_ist = app_start_time_utc.astimezone(IST)

    print("=" * 60)
    print("STATUS MONITOR - Starting up")
    print(f"Start Time (UTC): {app_start_time_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Start Time (IST): {app_start_time_ist.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("=" * 60)

    # Count providers by mode
    rss_count = sum(1 for p in PROVIDERS if p["mode"] == "rss")
    hash_count = sum(1 for p in PROVIDERS if p["mode"] == "hash")

    print(f"Providers configured: {len(PROVIDERS)}")
    print(f"  - RSS + ETag mode: {rss_count}")
    print(f"  - Hash polling mode: {hash_count}")
    print("=" * 60)

    # Start monitors for each provider
    for provider in PROVIDERS:
        if provider["mode"] == "rss":
            task = asyncio.create_task(rss_monitor(provider))
        elif provider["mode"] == "hash":
            task = asyncio.create_task(hash_monitor(provider))
        else:
            print(f"[WARN] Unknown mode for {provider['name']}: {provider['mode']}")
            continue

        background_tasks.append(task)

    print(f"\nStarted {len(background_tasks)} monitors")
    print("Waiting for incidents...\n")

    yield  # App runs here

    # Shutdown - cancel all tasks
    print("\nShutting down monitors...")
    for task in background_tasks:
        task.cancel()

    # Wait for tasks to finish
    await asyncio.gather(*background_tasks, return_exceptions=True)
    print("All monitors stopped")


# Create FastAPI app
app = FastAPI(
    title="Status Monitor",
    description="Monitors service status pages for incidents",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    """Serve the main UI page."""
    # Calculate stats
    rss_providers = [p for p in PROVIDERS if p["mode"] == "rss"]
    hash_providers = [p for p in PROVIDERS if p["mode"] == "hash"]

    # Calculate uptime
    now_utc = datetime.now(timezone.utc)
    uptime = now_utc - app_start_time_utc if app_start_time_utc else timedelta(0)
    uptime_str = str(uptime).split('.')[0]  # Remove microseconds

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "providers": PROVIDERS,
            "rss_providers": rss_providers,
            "hash_providers": hash_providers,
            "incidents": state.incidents[:50],  # Last 50 incidents
            "monitor_status": state.monitor_status,
            "total_providers": len(PROVIDERS),
            "rss_count": len(rss_providers),
            "hash_count": len(hash_providers),
            "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "start_time_utc": app_start_time_utc.strftime("%Y-%m-%d %H:%M:%S UTC") if app_start_time_utc else "N/A",
            "start_time_ist": app_start_time_ist.strftime("%Y-%m-%d %H:%M:%S IST") if app_start_time_ist else "N/A",
            "uptime": uptime_str
        }
    )


@app.get("/api/incidents")
async def get_incidents(limit: int = 50):
    """Get detected incidents."""
    return {
        "count": len(state.incidents),
        "incidents": state.incidents[:limit]
    }


@app.get("/api/providers")
async def get_providers():
    """Get configured providers and their status."""
    providers_with_status = []

    for provider in PROVIDERS:
        name = provider["name"]
        status_info = state.monitor_status.get(name, {})

        providers_with_status.append({
            "name": name,
            "mode": provider["mode"],
            "poll_interval": provider.get("poll_interval", 60),
            "url": provider.get("rss_url") or provider.get("api_url"),
            "status": status_info.get("status", "unknown"),
            "last_check": status_info.get("last_check"),
            "checks": status_info.get("checks", 0),
            "changes_detected": status_info.get("changes_detected", 0)
        })

    return {
        "total": len(PROVIDERS),
        "rss_count": sum(1 for p in PROVIDERS if p["mode"] == "rss"),
        "hash_count": sum(1 for p in PROVIDERS if p["mode"] == "hash"),
        "providers": providers_with_status
    }


@app.get("/api/health")
async def health():
    """Health check endpoint."""
    running_monitors = sum(
        1 for status in state.monitor_status.values()
        if status.get("status") == "running"
    )

    return {
        "status": "healthy",
        "monitors_running": running_monitors,
        "total_providers": len(PROVIDERS),
        "incidents_detected": len(state.incidents)
    }


# ============================================================
# TEST ENDPOINTS - For demonstration and testing
# ============================================================

@app.post("/api/test/incident")
async def create_test_incident(
    provider: str = "OpenAI",
    component: str = "Chat Completions API",
    message: str = "Elevated error rates detected",
    severity: str = "major"
):
    """Create a test incident for demonstration."""
    from core.handler import on_change

    await on_change(
        provider_name=provider,
        components=[component],
        message=message,
        status="investigating",
        severity=severity,
        incident_id=f"test-{datetime.now().timestamp()}",
        title=f"Test Incident - {component}"
    )

    return {
        "status": "created",
        "message": f"Test incident created for {provider}",
        "total_incidents": len(state.incidents)
    }


@app.get("/api/test/demo")
async def create_demo_incidents():
    """Create multiple sample incidents for demonstration."""
    from core.handler import on_change

    # Sample incidents matching real-world scenarios
    demo_incidents = [
        {
            "provider": "OpenAI",
            "components": ["Chat Completions API", "Responses API"],
            "message": "We are investigating elevated error rates on the API. Some requests may fail or experience increased latency.",
            "status": "investigating",
            "severity": "major",
            "title": "API Performance Degradation"
        },
        {
            "provider": "GitHub",
            "components": ["Actions", "API Requests"],
            "message": "GitHub Actions workflows may be delayed. We are working to resolve this issue.",
            "status": "identified",
            "severity": "minor",
            "title": "Actions Delays"
        },
        {
            "provider": "Stripe",
            "components": ["Payments API"],
            "message": "A small percentage of payment requests are failing. Our team is actively investigating.",
            "status": "investigating",
            "severity": "critical",
            "title": "Payment Processing Issues"
        },
        {
            "provider": "Cloudflare",
            "components": ["CDN", "DNS"],
            "message": "Increased DNS resolution times in EU regions. Mitigation in progress.",
            "status": "monitoring",
            "severity": "minor",
            "title": "EU DNS Latency"
        },
        {
            "provider": "Vercel",
            "components": ["Deployments", "Edge Functions"],
            "message": "Deployments may take longer than usual to complete.",
            "status": "identified",
            "severity": "minor",
            "title": "Deployment Delays"
        }
    ]

    for incident in demo_incidents:
        await on_change(
            provider_name=incident["provider"],
            components=incident["components"],
            message=incident["message"],
            status=incident["status"],
            severity=incident["severity"],
            incident_id=f"demo-{incident['provider'].lower()}-{datetime.now().timestamp()}",
            title=incident["title"]
        )

    return {
        "status": "created",
        "message": f"Created {len(demo_incidents)} demo incidents",
        "incidents": [i["provider"] + " - " + i["title"] for i in demo_incidents],
        "total_incidents": len(state.incidents)
    }


@app.get("/api/test/clear")
async def clear_test_incidents():
    """Clear only test/demo incidents (keeps real detected incidents)."""
    original_count = len(state.incidents)

    # Only remove incidents with test- or demo- prefix in their ID
    state.incidents[:] = [
        inc for inc in state.incidents
        if not (inc.get("id", "").startswith("test-") or inc.get("id", "").startswith("demo-"))
    ]

    cleared_count = original_count - len(state.incidents)
    return {
        "status": "cleared",
        "message": f"Cleared {cleared_count} test/demo incidents",
        "remaining": len(state.incidents)
    }


@app.get("/api/test/clear-all")
async def clear_all_incidents():
    """Clear ALL incidents (including real ones) - use with caution."""
    count = len(state.incidents)
    state.incidents.clear()
    return {
        "status": "cleared",
        "message": f"Cleared all {count} incidents"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
