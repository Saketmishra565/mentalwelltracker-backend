from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReminderBase(BaseModel):
    title: str
    message: str
    scheduled_time: datetime

class ReminderCreate(ReminderBase):
    user_id: int

class ReminderUpdate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    scheduled_time: Optional[datetime] = None
    user_id: Optional[int] = None

class ReminderRead(ReminderBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
