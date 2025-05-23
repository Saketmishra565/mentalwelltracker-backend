from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class CurrentIssue(Base):
    __tablename__ = "current_issues"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    issue = Column(String(255), nullable=False)

    user = relationship("User", back_populates="current_issues")
