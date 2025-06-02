import re
import random

def is_valid_email(email: str) -> bool:
    """
    Validate email format using regex.
    Returns True if valid, else False.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_otp() -> str:
    """
    Generate a 6-digit numeric OTP as a string.
    """
    return f"{random.randint(100000, 999999)}"
