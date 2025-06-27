from sqlalchemy import Column, String, Boolean, Integer
from app.database import Base

class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    notifications = Column(String)
    theme = Column(String)
    anonymous = Column(Boolean, default=False)
    language = Column(String)
    email = Column(String)
    password = Column(String)
