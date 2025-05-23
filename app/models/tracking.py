from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Tracking(Base):
    __tablename__ = "trackings"

    id = Column(Integer, primary_key=True, index=True)
    activity = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")
