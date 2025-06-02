from sqlalchemy import Column, String, DateTime
from app.database import Base

email = Column(String, primary_key=True, index=True)
otp = Column(String)
expires_at = Column(DateTime)