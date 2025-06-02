from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from datetime import datetime, timedelta
from app.models.email_verification import EmailVerification
from app.models.user import User
from app.utils.email_utils import send_otp_email
from app.utils.verification import generate_otp, is_valid_email

OTP_EXPIRE_MINUTES = 10

def create_otp_and_send_email(db: Session, email: str, background_tasks: BackgroundTasks = None):
    if not is_valid_email(email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_verified:
        return {"msg": "User already verified"}

    otp = generate_otp()

    verification = db.query(EmailVerification).filter(EmailVerification.user_id == user.id).first()
    if not verification:
        verification = EmailVerification(user_id=user.id, token=otp)
        db.add(verification)
    else:
        verification.token = otp
        verification.expires_at = datetime.utcnow() + timedelta(minutes=OTP_EXPIRE_MINUTES)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while saving OTP")

    if background_tasks:
        background_tasks.add_task(send_otp_email, email, otp)
    else:
        send_otp_email(email, otp)

    return {"msg": "Verification code sent via email."}

def verify_otp(db: Session, email: str, otp: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    verification = db.query(EmailVerification).filter(
        EmailVerification.user_id == user.id,
        EmailVerification.token == otp,
        EmailVerification.expires_at > datetime.utcnow()
    ).first()

    if not verification:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    user.is_verified = True
    verification.is_verified = True

    db.commit()

    return {"msg": "Email verified successfully"}
