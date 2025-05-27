from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.tracking import TrackingCreate, TrackingRead, TrackingUpdate
from app.models.tracking import Tracking
from app.services.tracking import (
    track_activity,
    get_tracking_data,
    get_tracking_by_id,
    update_tracking,
    delete_tracking,
)

router = APIRouter(prefix="/tracking", tags=["Tracking"])

@router.post("/", response_model=TrackingRead, status_code=status.HTTP_201_CREATED)
def add_tracking(data: TrackingCreate, db: Session = Depends(get_db)):
    return track_activity(db, data)

@router.get("/{user_id}", response_model=List[TrackingRead])
def get_user_tracking(user_id: int, db: Session = Depends(get_db)):
    return get_tracking_data(db, user_id)

@router.get("/item/{tracking_id}", response_model=TrackingRead)
def get_tracking_item(tracking_id: int, db: Session = Depends(get_db)):
    tracking = get_tracking_by_id(db, tracking_id)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking item not found")
    return tracking

@router.put("/item/{tracking_id}", response_model=TrackingRead)
def update_tracking_item(tracking_id: int, update_data: TrackingUpdate, db: Session = Depends(get_db)):
    updated = update_tracking(db, tracking_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Tracking item not found")
    return updated

@router.delete("/item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Tracking).filter(Tracking.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Tracking item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}


