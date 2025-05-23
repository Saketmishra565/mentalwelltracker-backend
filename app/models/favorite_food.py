from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base


class FavoriteFood(Base):
    __tablename__ = "favorite_food"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    food_name = Column(String(255), nullable=False)

    user = relationship("User", back_populates="favorite_food")
