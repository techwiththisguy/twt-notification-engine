import json
import urllib.request
from app import config
from app.store import log_delivery

def forward_webhook(payload: dict) -> None:
    if not config.FORWARD_WEBHOOK_URL:
        return
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        config.FORWARD_WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            log_delivery({"channel": "webhook", "status": "sent", "code": resp.status})
    except Exception as e:
        log_delivery({"channel": "webhook", "status": "failed", "error": str(e)})
        raise