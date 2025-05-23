from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class DailyRoutine(Base):
    __tablename__ = "daily_routine"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    activity = Column(String(255), nullable=False)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    notes = Column(String(500), nullable=True)

    user = relationship("User", back_populates="daily_routine")
