from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class MedicalInfo(Base):
    __tablename__ = "medical_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    blood_group = Column(String(10), nullable=True)
    allergies = Column(Text, nullable=True)       # JSON string or comma separated
    chronic_conditions = Column(Text, nullable=True)  # JSON string or comma separated
    medications = Column(Text, nullable=True)
    other_info = Column(Text, nullable=True)

    user = relationship("User", back_populates="medical_info")
