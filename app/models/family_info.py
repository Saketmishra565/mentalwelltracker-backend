from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base



class FamilyInfo(Base):
    __tablename__ = "family_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    father_name = Column(String(100), nullable=True)
    mother_name = Column(String(100), nullable=True)
    siblings = Column(Text, nullable=True)  # comma separated or JSON string
    other_family_members = Column(Text, nullable=True)

    user = relationship("User", back_populates="family_info")
