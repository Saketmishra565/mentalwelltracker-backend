from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String(100), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    contact_number = Column(String(20), nullable=True)
    favorite_work = Column(String(255), nullable=True)
    is_verified = Column(Boolean, default=False)

    email_verification = relationship("EmailVerification", back_populates="user", uselist=False)
    family_info = relationship("FamilyInfo", back_populates="user", uselist=False, cascade="all, delete")
    occupation_info = relationship("OccupationInfo", back_populates="user", uselist=False, cascade="all, delete")
    current_challenges = relationship("CurrentChallenge", back_populates="user", cascade="all, delete-orphan")
    current_issues = relationship("CurrentIssue", back_populates="user", cascade="all, delete-orphan")
    daily_routine = relationship("DailyRoutine", back_populates="user", uselist=False, cascade="all, delete")
    education_info = relationship("EducationInfo", back_populates="user", uselist=False, cascade="all, delete")
    favorite_food = relationship("FavoriteFood", back_populates="user", uselist=False, cascade="all, delete")
    hobbies = relationship("Hobby", back_populates="user", cascade="all, delete-orphan")
    skills = relationship("Skill", back_populates="user", cascade="all, delete-orphan")
    important_dates = relationship("ImportantDate", back_populates="user", cascade="all, delete-orphan")
    marital_info = relationship("MaritalInfo", back_populates="user", uselist=False, cascade="all, delete")
    medical_info = relationship("MedicalInfo", back_populates="user", uselist=False, cascade="all, delete")
    motivation = relationship("Motivation", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    other_information = relationship("OtherInformation", back_populates="user", uselist=False, cascade="all, delete")
    past_incidents = relationship("PastIncident", back_populates="user", cascade="all, delete-orphan")
    reminders = relationship("Reminder", back_populates="user", cascade="all, delete-orphan")
    trackings = relationship("Tracking", back_populates="user", cascade="all, delete-orphan")
    user_profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
    
