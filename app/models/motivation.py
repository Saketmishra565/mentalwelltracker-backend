from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Motivation(Base):
    __tablename__ = "motivations"

    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String, index=True)
    author = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="motivations")
