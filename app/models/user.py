# app/models/user.py

from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime, timedelta

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    full_name = Column(String(100), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    contact_number = Column(String(20), nullable=True)
    favorite_work = Column(String(255), nullable=True)

    verification_token = Column(String, unique=True, index=True)
    verification_expiry = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(minutes=10))
    is_verified = Column(Boolean, default=False)

    # Relationships
    family_info = relationship("FamilyInfo", back_populates="user", cascade="all, delete", uselist=False)
    occupation_info = relationship("OccupationInfo", back_populates="user", cascade="all, delete", uselist=False)
    marital_info = relationship("MaritalInfo", back_populates="user", cascade="all, delete", uselist=False)
    medical_info = relationship("MedicalInfo", back_populates="user", cascade="all, delete", uselist=False)

    current_challenges = relationship("CurrentChallenge", back_populates="user", cascade="all, delete")
    current_issues = relationship("CurrentIssue", back_populates="user", cascade="all, delete")
    daily_routine = relationship("DailyRoutine", back_populates="user", cascade="all, delete")
    education_info = relationship("EducationInfo", back_populates="user", cascade="all, delete")
    favorite_food = relationship("FavoriteFood", back_populates="user", cascade="all, delete")
    hobbies = relationship("Hobby", back_populates="user", cascade="all, delete")
    skills = relationship("Skill", back_populates="user", cascade="all, delete")
    important_dates = relationship("ImportantDate", back_populates="user", cascade="all, delete")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    past_incidents = relationship("PastIncident", back_populates="user", cascade="all, delete-orphan")
    reminders = relationship("Reminder", back_populates="user", cascade="all, delete-orphan")

    other_information = relationship(
        "OtherInformation",
        back_populates="user",
        cascade="all, delete",
        uselist=False
    )

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
