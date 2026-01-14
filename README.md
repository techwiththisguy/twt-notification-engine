# TWT Notification Engine

TWT Notification Engine is a lightweight event ingestion service built with FastAPI.
It receives lead-related events and routes notifications (email/webhooks) so small businesses never miss an inquiry.

## Why this exists
Small service businesses get leads from multiple sources (website, Facebook, text, calls).
Follow-ups can slip. This service creates a single “notification brain” that other apps can call.

## Features
- FastAPI service with Swagger docs
- Lead event ingest endpoint: `POST /events/lead`
- Health endpoint: `GET /health`
- Notification adapters (email/webhook) designed for extension
- Config driven via environment variables (no secrets in repo)

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic

## Example Payload

{
  "event_type": "lead_created",
  "source": "twt-lead-assurance",
  "lead_id": 2,
  "name": "Patrick Wilder",
  "phone": "555-555-5555",
  "service_type": "Land Clearing",
  "location": "Lakeland, FL",
  "notes": "Customer wants quote for clearing 1 acre. Prefers text updates.",
  "status": "NEW",
  "meta": {
    "channel": "website",
    "client": "Conner Land Solutions"
  }
}

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload --host 127.0.0.1 --port 8080