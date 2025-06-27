from typing import Optional, List
from datetime import date
from pydantic import BaseModel, EmailStr


class EducationInfo(BaseModel):
    degree: Optional[str]
    institution: Optional[str]
    year_of_passing: Optional[int]
    percentage_or_grade: Optional[str]

    class Config:
        from_attributes = True


class ImportantDate(BaseModel):
    event_name: Optional[str]
    date: Optional[date]

    class Config:
        from_attributes = True


class DailyRoutine(BaseModel):
    wake_up_time: Optional[str]  # e.g. "06:30 AM"
    sleep_time: Optional[str]    # e.g. "10:30 PM"
    activities: Optional[List[str]]

    class Config:
        from_attributes = True


class MedicalInfo(BaseModel):
    blood_group: Optional[str]
    allergies: Optional[List[str]]
    chronic_diseases: Optional[List[str]]
    medications: Optional[List[str]]

    class Config:
        from_attributes = True


class FamilyInfo(BaseModel):
    father_name: Optional[str]
    mother_name: Optional[str]
    siblings: Optional[List[str]]
    other_family_members: Optional[str]

    class Config:
        from_attributes = True


class OccupationInfo(BaseModel):
    current_job: Optional[str]
    company_name: Optional[str]
    designation: Optional[str]
    years_of_experience: Optional[int]
    previous_jobs: Optional[List[str]]

    class Config:
        from_attributes = True


class MaritalInfo(BaseModel):
    marital_status: Optional[str]
    life_partner_name: Optional[str]
    anniversary_date: Optional[date]

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    address: Optional[str] = None

    family_info: Optional[FamilyInfo] = None
    occupation_info: Optional[OccupationInfo] = None
    medical_info: Optional[MedicalInfo] = None
    education_info: Optional[List[EducationInfo]] = None
    marital_info: Optional[MaritalInfo] = None

    hobbies: Optional[List[str]] = None
    skills: Optional[List[str]] = None
    favorite_work: Optional[str] = None
    daily_routine: Optional[DailyRoutine] = None
    favorite_food: Optional[List[str]] = None
    past_incidents: Optional[List[str]] = None
    current_issues: Optional[List[str]] = None
    current_challenges: Optional[List[str]] = None
    important_dates: Optional[List[ImportantDate]] = None
    other_information: Optional[str] = None

    class Config:
        from_attributes = True
class UserRead(UserBase):
    id: int
    full_name: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    address: Optional[str]

    family_info: Optional[FamilyInfo]
    occupation_info: Optional[OccupationInfo]
    medical_info: Optional[MedicalInfo]
    education_info: Optional[List[EducationInfo]]
    marital_info: Optional[MaritalInfo]

    hobbies: Optional[List[str]]
    skills: Optional[List[str]]
    favorite_work: Optional[str]
    daily_routine: Optional[DailyRoutine]
    favorite_food: Optional[List[str]]
    past_incidents: Optional[List[str]]
    current_issues: Optional[List[str]]
    current_challenges: Optional[List[str]]
    important_dates: Optional[List[ImportantDate]]
    other_information: Optional[str]

    class Config:
        from_attributes = True


class SignupResponse(BaseModel):
    message: str
    email: EmailStr


class VerifyRequest(BaseModel):
    token: str


class ResendRequest(BaseModel):
    email: EmailStr


class OTPSendRequest(BaseModel):
    email: EmailStr


class OTPVerifyRequest(BaseModel):
    email: EmailStr
    otp: str
