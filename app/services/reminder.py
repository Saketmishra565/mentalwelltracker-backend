from sqlalchemy.orm import Session
from app.models.reminder import Reminder

def create_reminder(db: Session, data):
    from app.schemas.reminder import ReminderCreate
    reminder = Reminder(**data.dict())
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return reminder

def get_reminders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reminder).offset(skip).limit(limit).all()

def get_reminder_by_id(db: Session, reminder_id: int):
    return db.query(Reminder).filter(Reminder.id == reminder_id).first()

def update_reminder(db: Session, reminder_id: int, data):
    from app.schemas.reminder import ReminderUpdate
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(reminder, key, value)
    db.commit()
    db.refresh(reminder)
    return reminder

def delete_reminder(db: Session, reminder_id: int):
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        return None
    db.delete(reminder)
    db.commit()
    return reminder
