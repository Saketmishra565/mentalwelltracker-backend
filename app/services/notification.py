from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate

def create_notification(db: Session, data: NotificationCreate):
    notification = Notification(**data.dict())
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

def get_user_notifications(db: Session, user_id: int):
    return db.query(Notification).filter(Notification.user_id == user_id).all()

def get_notification_by_id(db: Session, notification_id: int):
    return db.query(Notification).filter(Notification.id == notification_id).first()

def update_notification(db: Session, notification_id: int, update_data: NotificationUpdate):
    notification = get_notification_by_id(db, notification_id)
    if not notification:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(notification, key, value)
    db.commit()
    db.refresh(notification)
    return notification

def delete_notification(db: Session, notification_id: int):
    notification = get_notification_by_id(db, notification_id)
    if not notification:
        return None
    db.delete(notification)
    db.commit()
    return notification
