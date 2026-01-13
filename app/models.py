from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class LeadEvent(BaseModel):
    event_type: str = Field(..., examples=["lead_created", "lead.status_updated"])
    source: str = Field(..., examples=["twt-lead-assurance"])
    lead_id: Optional[int] = None
    
    name: Optional[str] = None
    phone: Optional[str] = None
    service_type: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None
    
    meta: Dict[str, Any] = {}