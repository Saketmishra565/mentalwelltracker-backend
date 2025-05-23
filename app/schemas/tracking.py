from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TrackingBase(BaseModel):
    activity: str
    timestamp: datetime

class TrackingCreate(TrackingBase):
    user_id: int

class TrackingUpdate(BaseModel):
    activity: Optional[str] = None
    timestamp: Optional[datetime] = None

class TrackingRead(TrackingBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
