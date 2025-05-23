from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NotificationBase(BaseModel):
    message: str
    created_at: datetime
    read: bool = False

class NotificationCreate(NotificationBase):
    user_id: int

class NotificationUpdate(BaseModel):
    message: Optional[str] = None
    created_at: Optional[datetime] = None
    read: Optional[bool] = None

class NotificationRead(NotificationBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
