from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging  # Add logging

from app.schemas.auth import (
    UserLogin,
    UserRegister,
    ResetPassword,
    LoginResponse
)
from app.services.auth import login_user, register_user, reset_password
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

logger = logging.getLogger(__name__)  # Logger instance


@router.post("/login", response_model=LoginResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user(db, data.username, data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /login: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


@router.post("/register", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):
    try:
        register_user(db, data.username, data.email, data.password)
        return login_user(db, data.username, data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /register: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


@router.post("/reset-password", status_code=status.HTTP_200_OK)
def reset_user_password(data: ResetPassword, db: Session = Depends(get_db)):
    try:
        return reset_password(db, data.email, data.new_password)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /reset-password: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
