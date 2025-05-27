import jwt
from datetime import datetime, timedelta

from app.utils.config import settings  # अगर तुम्हारा config.py settings देता है

SECRET_KEY = settings.SECRET_KEY  # .env से लेने के लिए config.py में सेट होना चाहिए
ALGORITHM = "HS256"
VERIFICATION_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 घंटे

def generate_verification_token(email: str):
    expire = datetime.utcnow() + timedelta(minutes=VERIFICATION_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_verification_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.PyJWTError:
        raise Exception("Invalid token")
