from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class ImportantDate(Base):
    __tablename__ = "important_dates"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String(255), nullable=False)        # जैसे "Birthday", "Anniversary"
    date = Column(Date, nullable=False)
    description = Column(String(500), nullable=True)

    user = relationship("User", back_populates="important_dates")
