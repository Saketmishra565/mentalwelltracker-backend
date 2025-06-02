from pydantic import BaseModel, EmailStr, constr
from typing import Annotated

class UserRegister(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=50)]
    email: EmailStr
    password: Annotated[str, constr(min_length=6)]

class UserLogin(BaseModel):
    username: str
    password: str

class ResetPassword(BaseModel):
    email: EmailStr
    new_password: Annotated[str, constr(min_length=6)]

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    message: str = None

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

class VerifyRequest(BaseModel):
    token: str
