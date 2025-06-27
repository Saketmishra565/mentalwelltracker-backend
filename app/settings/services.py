from sqlalchemy.orm import Session
from . import models, schemas

def save_user_settings(db: Session, settings: schemas.SettingsCreate):
    db_settings = models.UserSettings(**settings.dict())
    db.add(db_settings)
    db.commit()
    db.refresh(db_settings)
    return db_settings

def get_user_settings(db: Session):
    return db.query(models.UserSettings).first()
