from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks
from app.models.user import User
from app.utils.email_utils import send_verification_email
from app.utils.token_utils import generate_verification_token, decode_verification_token

def create_verification_token_and_send_email(db, user, background_tasks):
    token = generate_verification_token(user.email)
    
    if background_tasks:
        # Email ko background mein bhejne ke liye task add karo
        background_tasks.add_task(send_verification_email, user.email, token)
    else:
        # Agar background tasks nahi hai, to sync bhejo
        send_verification_email(user.email, token)
    
    return {"msg": "Verification email sent"}

def verify_email_token(db: Session, token: str):
    email = decode_verification_token(token)
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_verified:
        return {"msg": "User already verified"}
    user.is_verified = True
    db.commit()
    return {"msg": "Email verified successfully"}

def resend_verification_email(db: Session, email: str, background_tasks: BackgroundTasks = None):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_verified:
        return {"msg": "User already verified"}
    return create_verification_token_and_send_email(db, user, background_tasks)
