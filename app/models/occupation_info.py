# models/occupation_information.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class OccupationInfo(Base):
    __tablename__ = "occupation_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)  # ✅ FIXED HERE
    occupation_type = Column(String(100))
    company = Column(String(100))

    user = relationship("User", back_populates="occupation_info")
