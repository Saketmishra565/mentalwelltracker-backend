from pydantic import BaseModel
from typing import Optional
from app.models.base import Base
from sqlalchemy import Column, Integer, String

class MotivationBase(BaseModel):
    quote: str
    author: str

class MotivationCreate(MotivationBase):
    pass

class Motivation(Base):
    __tablename__ = "motivations"
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String, index=True)
    author = Column(String)

class MotivationRead(MotivationBase):
    id: int

    class Config:
       from_attributes = True
