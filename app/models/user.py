from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    contact_number = Column(String(20), nullable=True)
    favorite_work = Column(String(255), nullable=True)

    # One-to-one relationships
    family_info = relationship("FamilyInfo", back_populates="user", cascade="all, delete", uselist=False)
    occupation_info = relationship("OccupationInfo", back_populates="user", cascade="all, delete", uselist=False)
    current_challenges = relationship("CurrentChallenge", back_populates="user", cascade="all, delete")
    current_issues = relationship("CurrentIssue", back_populates="user", cascade="all, delete")
    daily_routine = relationship("DailyRoutine", back_populates="user", cascade="all, delete")
    education_info = relationship("EducationInfo", back_populates="user", cascade="all, delete", uselist=False)
    favorite_food = relationship("FavoriteFood", back_populates="user", cascade="all, delete", uselist=False)
    hobbies = relationship("Hobby", back_populates="user", cascade="all, delete")
    skills = relationship("Skill", back_populates="user", cascade="all, delete")
    important_dates = relationship("ImportantDate", back_populates="user", cascade="all, delete")
    marital_info = relationship("MaritalInfo", back_populates="user", cascade="all, delete", uselist=False)
    medical_info = relationship("MedicalInfo", back_populates="user", cascade="all, delete", uselist=False)
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
    other_information = relationship("OtherInformation", back_populates="user", uselist=False)
    past_incidents = relationship("PastIncident", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
