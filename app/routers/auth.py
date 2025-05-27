from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
import logging

from app.schemas.auth import (
    UserLogin,
    UserRegister,
    ResetPassword,
    LoginResponse
)
from app.schemas.user import VerifyRequest, ResendRequest
from app.services.auth import login_user, register_user, reset_password
from app.services.verification import (
    create_verification_token_and_send_email,
    verify_email_token,
    resend_verification_email
)

from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

logger = logging.getLogger(__name__)


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

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db), background_tasks: BackgroundTasks = None):
    try:
        user = register_user(db, data.username, data.email, data.password)

        # Send verification email using background tasks
        create_verification_token_and_send_email(db, user, background_tasks)

        return {"message": "Verification email sent. Please verify your account."}
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


@router.post("/verify-email")
def verify_email(req: VerifyRequest, db: Session = Depends(get_db)):
    try:
        verify_email_token(db, req.token)
        return {"message": "Email verified successfully."}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /verify-email: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


@router.post("/resend-verification")
def resend_verification(req: ResendRequest, db: Session = Depends(get_db), background_tasks: BackgroundTasks = None):
    try:
        resend_verification_email(db, req.email, background_tasks)
        return {"message": "Verification email resent."}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /resend-verification: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

@router.get("/verify-test/{username}")
def verify_test_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_verified = True
    db.commit()
    return {"msg": f"User {username} verified for testing"}
