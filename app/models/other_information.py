# app/models/other_information.py

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class OtherInformation(Base):
    __tablename__ = "other_information"

    id = Column(Integer, primary_key=True)
    info = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)  # unique=True for one-to-one

    user = relationship("User", back_populates="other_information")
