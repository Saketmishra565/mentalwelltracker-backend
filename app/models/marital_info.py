from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class MaritalInfo(Base):
    __tablename__ = "marital_info"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    marital_status = Column(String(50), nullable=True)  # e.g. Married, Single
    spouse_name = Column(String(100), nullable=True)
    anniversary_date = Column(Date, nullable=True)
    children = Column(String(255), nullable=True)  # JSON string or comma separated

    user = relationship("User", back_populates="marital_info")
