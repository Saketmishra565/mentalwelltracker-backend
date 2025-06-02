from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.reminder import ReminderCreate, ReminderRead, ReminderUpdate
from typing import List
from app.database import get_db
from app.services.reminder import (
    create_reminder,
    get_reminders,
    get_reminder_by_id,
    update_reminder,
    delete_reminder,
)
from app.models.reminder import Reminder

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.post("/", response_model=ReminderRead, status_code=status.HTTP_201_CREATED)
def add_reminder(reminder: ReminderCreate, db: Session = Depends(get_db)):
    return create_reminder(db, reminder)

@router.get("/", response_model=List[ReminderRead])
def list_reminders(db: Session = Depends(get_db)):
    return get_reminders(db)

@router.get("/{reminder_id}", response_model=ReminderRead)
def read_reminder(reminder_id: int, db: Session = Depends(get_db)):
    reminder = get_reminder_by_id(db, reminder_id)
    if not reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")
    return reminder

@router.put("/{reminder_id}", response_model=ReminderRead)
def update_reminder_data(reminder_id: int, reminder_update: ReminderUpdate, db: Session = Depends(get_db)):
    updated_reminder = update_reminder(db, reminder_id, reminder_update)
    if not updated_reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")
    return updated_reminder

@router.delete("/{reminder_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    reminder = db.query(Reminder).filter(Reminder.id == reminder_id).first()
    if not reminder:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reminder not found")

    db.delete(reminder)
    db.commit()
    return
