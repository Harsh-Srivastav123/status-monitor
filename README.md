# Status Monitor

A Python application that automatically tracks and logs service updates from multiple status pages (OpenAI, GitHub, Stripe, etc.).

## Features

- **Efficient Monitoring**: Uses RSS + ETag for minimal bandwidth (304 when unchanged)
- **Fallback Support**: Hash-based polling for providers without RSS feeds
- **Scalable**: AsyncIO handles 100+ providers concurrently in a single thread
- **Real-time Console Output**: Prints incidents as they're detected
- **Web UI**: Simple auto-refresh page showing providers and incidents
- **REST API**: JSON endpoints for programmatic access

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MONITORS                             │
│                                                         │
│   RSS + ETag Monitor          Hash Polling Monitor      │
│   (Primary - efficient)       (Fallback)                │
│                                                         │
│   Every 60s:                  Every 60s:                │
│   GET feed + If-None-Match    GET endpoint              │
│   304? → sleep               SHA256 hash body           │
│   200? → parse               Same? → sleep              │
│                              Different? → parse         │
└─────────────────────┬─────────────────────┬────────────┘
                      │                     │
                      └──────────┬──────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   on_change() handler  │
                    │                        │
                    │   1. Print to console  │
                    │   2. Store in memory   │
                    └────────────────────────┘
```

## Quick Start

### Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

Open http://localhost:8000 to see the UI.

### Run with Docker

```bash
# Build and run
docker-compose up --build

# Or manually
docker build -t status-monitor .
docker run -p 8000:8000 status-monitor
```

## Console Output Example

```
[2025-11-03 14:32:00] Product: OpenAI - Chat Completions API
Status: Elevated error rates detected on the API
Incident: API Performance Degradation
Severity: MAJOR
────────────────────────────────────────────────────────────
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Web UI with providers and incidents |
| `GET /api/incidents` | JSON list of detected incidents |
| `GET /api/providers` | JSON list of configured providers |
| `GET /api/health` | Health check |

## Adding Providers

Edit `config.py` to add new providers:

```python
# RSS + ETag mode (preferred)
{
    "name": "NewProvider",
    "mode": "rss",
    "rss_url": "https://status.newprovider.com/history.atom",
    "poll_interval": 60
}

# Hash polling mode (fallback)
{
    "name": "AnotherProvider",
    "mode": "hash",
    "api_url": "https://status.another.com/api/v2/incidents.json",
    "poll_interval": 60
}
```

## Configured Providers

### RSS + ETag Mode (Efficient)
- OpenAI
- GitHub
- Stripe
- Cloudflare
- Slack
- Twilio
- Datadog
- Atlassian
- Vercel
- Netlify
- DigitalOcean
- MongoDB
- Redis
- Heroku

### Hash Polling Mode (Fallback)
- Render
- Fly.io

## Deployment (Render.com)

1. Push to GitHub
2. Create new Web Service on Render
3. Connect your repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 8000`
5. Deploy

## Why This Approach?

| Requirement | Solution |
|-------------|----------|
| "Not inefficient polling" | RSS + ETag (304 = zero bandwidth) |
| "Event-based approach" | React only when content changes |
| "Scale to 100+ providers" | AsyncIO - single thread, concurrent |
| "Console output" | Print to stdout on every incident |
| "Lightweight app" | FastAPI + 5 dependencies |

## Project Structure

```
status-monitor/
├── main.py              # FastAPI app + startup
├── config.py            # Provider definitions
├── monitors/
│   ├── rss_monitor.py   # RSS + ETag monitor
│   └── hash_monitor.py  # Hash polling monitor
├── parsers/
│   └── statuspage.py    # RSS/JSON parsers
├── core/
│   ├── handler.py       # Event handler (print + store)
│   └── state.py         # In-memory state
├── templates/
│   └── index.html       # Web UI
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## License

MIT
