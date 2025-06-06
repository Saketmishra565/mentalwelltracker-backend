from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.notification import NotificationCreate, NotificationRead, NotificationUpdate
from app.services.notification import (
    create_notification,
    get_user_notifications,
    get_notification_by_id,
    update_notification,
    delete_notification,
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])

# CREATE
@router.post("/", response_model=NotificationRead, status_code=status.HTTP_201_CREATED)
def add_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    return create_notification(db, notification)

# READ (All for user)
@router.get("/{user_id}", response_model=List[NotificationRead])
def get_notifications(user_id: int, db: Session = Depends(get_db)):
    return get_user_notifications(db, user_id)

# READ (By id)
@router.get("/detail/{notification_id}", response_model=NotificationRead)
def get_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = get_notification_by_id(db, notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

# UPDATE
@router.put("/{notification_id}", response_model=NotificationRead)
def update_notification_endpoint(notification_id: int, update_data: NotificationUpdate, db: Session = Depends(get_db)):
    updated = update_notification(db, notification_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Notification not found")
    return updated

# DELETE
@router.delete("/notifications/user/{user_id}", summary="Delete all notifications for a user")
def delete_notifications_by_user(user_id: int, db: Session = Depends(get_db)):
    notifications = db.query(Notification).filter(Notification.user_id == user_id).all()
    if not notifications:
        raise HTTPException(status_code=404, detail="No notifications found for this user")

    for notification in notifications:
        db.delete(notification)
    db.commit()
    return {"message": f"All notifications for user {user_id} deleted successfully"}

