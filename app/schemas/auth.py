from pydantic import BaseModel, EmailStr, Field


class UserLogin(BaseModel):
    username: str
    password: str


class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class ResetPassword(BaseModel):
    email: EmailStr
    new_password: str = Field(..., min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str | None = None  # For verifying token payload


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str

    class Config:
        from_attributes = True
