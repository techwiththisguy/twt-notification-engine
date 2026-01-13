import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any

LOG_PATH = Path("delivery_log.json1")

def log_delivery(record: Dict[str, Any]) -> None:
    record["ts"] = datetime.now(timezone.utc).isoformat()
    with LOG_PATH.open("a", encoding="utf-8")as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")