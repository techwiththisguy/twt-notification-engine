from fastapi import FastAPI, HTTPException
from app.config import APP_NAME
from app.models import LeadEvent
from app.notifier_email import send_email
from app.notifier_webhook import forward_webhook
from app.store import log_delivery

app = FastAPI(title=APP_NAME)

@app.get("/health")
def health():
    return {"ok": True, "Service": APP_NAME}

@app.post("/events/lead")
def handle_lead_event(evt: LeadEvent):
    # Build a useful notification message
    subject = f"[{evt.event_type}] New update from {evt.source}"
    body = "\n".join([
        f"Event: {evt.event_type}",
        f"Source: {evt.source}",
        f"Lead ID: {evt.lead_id}",
        "",
        f"Name: {evt.name}",
        f"Phone: {evt.phone}",
        f"Service: {evt.service_type}",
        f"Location: {evt.location}",
        f"Status: {evt.status}",
        "",
        "Notes:",
        evt.notes or "",
    ])
    
    results = {"email": None, "webhook": None}
    
    # Try email (don't crach if it fails)
    try:
        # Send email + optional webhook forward
        send_email(subject, body)
        results["email"] = "sent"
    except Exception as e:
        results["email"] = f"failed: {e}"
        log_delivery({"channel": "email", "status": "failed", "error": str(e)})

    # Try webhook forward (don't crash if it fails)
    try:
        forward_webhook(evt.model_dump())
        results["webhook"] = "sent" if results["webhook"] is None else results["webhook"]
    except Exception as e:
        results["webhook"] = f"Faild: {e}"
        log_delivery({"channel": "webhook", "status": "failed", "error": str(e)})
        
    # Always acknowledge receipt
    return {"ok": True, "received": True, "results": results}        