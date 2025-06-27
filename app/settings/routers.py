from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from . import services, schemas

router = APIRouter()

@router.post("/settings", response_model=schemas.SettingsOut)
def save_settings(settings: schemas.SettingsCreate, db: Session = Depends(get_db)):
    return services.save_user_settings(db, settings)

@router.get("/settings", response_model=schemas.SettingsOut)
def read_settings(db: Session = Depends(get_db)):
    settings = services.get_user_settings(db)
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings
