from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from urllib.parse import unquote
from datetime import timedelta
import logging

from app.schemas.auth import (
    UserLogin,
    UserRegister,
    ResetPassword,
    LoginResponse,
    TokenSchema,
)
from app.schemas.user import VerifyRequest
from app.services.auth import (
    login_user,
    register_user,
    reset_password  
)
from app.services.verification import create_otp_and_send_email, verify_otp
from app.database import get_db
from app.models.user import User
from app.auth.jwt import create_access_token, create_refresh_token

# ✅ Router Setup with Prefix
router = APIRouter(prefix="/auth", tags=["Authentication"])
logger = logging.getLogger(__name__)

# ✅ Token Expiry Constants
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# ✅ Register Route
@router.post("/register", response_model=TokenSchema, status_code=status.HTTP_201_CREATED)
def register(
    data: UserRegister,
    db: Session = Depends(get_db),
    background_tasks: BackgroundTasks = None,
):
    try:
        user = register_user(db, data.username, data.email, data.password)

        # Send OTP via email
        create_otp_and_send_email(db, user.email, background_tasks)

        # Generate tokens
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        refresh_token = create_refresh_token(
            data={"sub": user.email},
            expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "message": "Verification code sent via email. Please verify your account.",
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /register: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ✅ Login Route
@router.post("/login", response_model=LoginResponse)
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        return login_user(db, data.username, data.password)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /login: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ✅ Reset Password Route
@router.post("/reset-password", status_code=status.HTTP_200_OK)
def reset_user_password(data: ResetPassword, db: Session = Depends(get_db)):
    try:
        return reset_password(db, data.email, data.new_password)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /reset-password: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ✅ Verify OTP
@router.post("/verify-otp")
def verify_email_otp(data: VerifyRequest, db: Session = Depends(get_db)):
    try:
        token_parts = data.token.split(":")
        if len(token_parts) != 2:
            raise HTTPException(status_code=400, detail="Invalid token format")

        email, otp = token_parts
        result = verify_otp(db, email, otp)
        return result

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in /verify-otp: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

# ✅ Testing Route for Verification
@router.get("/verify-test-by-email/{email}")
def verify_test_email(email: str, db: Session = Depends(get_db)):
    email = unquote(email)
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_verified = True
    db.commit()
    return {"msg": f"User with email '{email}' verified successfully for testing."}

