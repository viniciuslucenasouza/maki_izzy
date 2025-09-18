from pydantic import BaseModel
from typing import Dict, Any

class Event(BaseModel):
    source: str
    data: Dict[str, Any]

class Message(BaseModel):
    content: str

class PreviewRequest(BaseModel):
    event: Event
    template: str
