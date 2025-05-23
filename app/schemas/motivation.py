from typing import Optional
from pydantic import BaseModel

class MotivationBase(BaseModel):
    quote: str
    author: str

class MotivationCreate(MotivationBase):
    pass

class MotivationUpdate(BaseModel):
    quote: Optional[str] = None
    author: Optional[str] = None

class MotivationRead(MotivationBase):
    id: int

    class Config:
        from_attributes = True
