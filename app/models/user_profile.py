# app/models/user_profile.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bio = Column(String(255), nullable=True)
    profile_picture = Column(String(255), nullable=True)

    # Change here: 'profile' ko 'user_profile' se replace kiya hai
    user = relationship("User", back_populates="user_profile")

    def __repr__(self):
        return f"<UserProfile(user_id={self.user_id})>"
