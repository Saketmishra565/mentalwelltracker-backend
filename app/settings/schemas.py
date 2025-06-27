from pydantic import BaseModel

class SettingsBase(BaseModel):
    notifications: list[str]
    theme: str
    anonymous: bool
    language: str
    email: str
    password: str

class SettingsCreate(SettingsBase):
    pass

class SettingsOut(SettingsBase):
    pass
