from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.password import hash_password
import logging

logger = logging.getLogger(__name__)

# CREATE user with unique username/email check
def create_user(db: Session, user: UserCreate) -> Optional[User]:
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()
    if existing_user:
        logger.warning("Username or email already exists")
        return None  # या आप HTTPException भी raise कर सकते हैं

    hashed_pwd = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pwd
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error while creating user: {e}")
        return None

# GET user by username
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

# GET user by ID with eager loading of related info
def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return (
        db.query(User)
        .options(
            joinedload(User.family_info),
            joinedload(User.occupation_info),
            joinedload(User.medical_info),
            joinedload(User.education_info),
            joinedload(User.marital_info),
        )
        .filter(User.id == user_id)
        .first()
    )

# GET all users with pagination and eager loading
def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return (
        db.query(User)
        .options(
            joinedload(User.family_info),
            joinedload(User.occupation_info),
            joinedload(User.medical_info),
            joinedload(User.education_info),
            joinedload(User.marital_info),
        )
        .offset(skip)
        .limit(limit)
        .all()
    )

# UPDATE user by ID
def update_user(db: Session, user_id: int, update_data: UserUpdate) -> Optional[User]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    update_fields = update_data.dict(exclude_unset=True)

    if "password" in update_fields:
        user.hashed_password = hash_password(update_fields.pop("password"))

    for key, value in update_fields.items():
        setattr(user, key, value)

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Error updating user: {e}")
        return None

# DELETE user by ID
def delete_user(db: Session, user_id: int) -> Optional[User]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    try:
        db.delete(user)
        db.commit()
        return user
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting user: {e}")
        return None
