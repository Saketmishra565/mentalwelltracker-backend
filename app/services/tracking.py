from sqlalchemy.orm import Session
from app.models.tracking import Tracking
from app.schemas.tracking import TrackingCreate, TrackingUpdate

def track_activity(db: Session, data: TrackingCreate):
    tracking = Tracking(**data.dict())
    db.add(tracking)
    db.commit()
    db.refresh(tracking)
    return tracking

def get_tracking_data(db: Session, user_id: int):
    return db.query(Tracking).filter(Tracking.user_id == user_id).all()

def get_tracking_by_id(db: Session, tracking_id: int):
    return db.query(Tracking).filter(Tracking.id == tracking_id).first()

def update_tracking(db: Session, tracking_id: int, update_data: TrackingUpdate):
    tracking = get_tracking_by_id(db, tracking_id)
    if not tracking:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(tracking, key, value)
    db.commit()
    db.refresh(tracking)
    return tracking

def delete_tracking(db: Session, tracking_id: int):
    tracking = get_tracking_by_id(db, tracking_id)
    if not tracking:
        return None
    db.delete(tracking)
    db.commit()
    return tracking
