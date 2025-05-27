from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user import (
    create_user,
    get_user_by_id,
    get_user_by_username,
    get_users,
    update_user,
    delete_user,
)
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users Profile"])

# CREATE - Register new user
@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already registered")
    return create_user(db, user)

# READ - List all users
@router.get("/", response_model=List[UserRead])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

# READ - Get single user by ID
@router.get("/{user_id}", response_model=UserRead)
def get_single_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# UPDATE - Update user by ID
@router.put("/{user_id}", response_model=UserRead)
def update_single_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user

# DELETE - Delete user by ID
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None
