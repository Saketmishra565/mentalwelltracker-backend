from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class PastIncident(Base):
    __tablename__ = "past_incidents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String(255), nullable=False)
    incident_date = Column(Date, nullable=True)
    description = Column(Text, nullable=True)

    user = relationship("User", back_populates="past_incidents")
