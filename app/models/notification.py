from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255))
    created_at = Column(DateTime, nullable=False)
    read = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Optional relationship
    user = relationship("User", back_populates="notifications")
