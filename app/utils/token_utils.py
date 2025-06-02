
import jwt
from datetime import datetime, timedelta
from jwt import ExpiredSignatureError, InvalidTokenError
from typing import Optional

# Import your settings/config with SECRET_KEY etc.
from app.utils.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
VERIFICATION_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

def generate_verification_token(email: str) -> str:
    """
    Generate a JWT token encoding the user's email.
    Token expires in 24 hours by default.
    """
    expire = datetime.utcnow() + timedelta(minutes=VERIFICATION_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_verification_token(token: str) -> Optional[str]:
    """
    Decode a JWT token and return the email (sub).
    Raises Exception on invalid/expired token.
    """
    try:
        if token.count('.') != 2:
            raise Exception("Invalid token format")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise Exception("Email not found in token")
        return email

    except ExpiredSignatureError:
        raise Exception("Token expired")
    except InvalidTokenError:
        raise Exception("Invalid token")
