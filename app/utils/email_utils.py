import smtplib
from email.mime.text import MIMEText
from app.utils.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USERNAME, EMAIL_PASSWORD

def send_otp_email(to_email: str, otp: str):
    body = f"Your verification code is: {otp}. Please enter this code to verify your email."

    msg = MIMEText(body)
    msg['Subject'] = "Email Verification Code"
    msg['From'] = EMAIL_USERNAME
    msg['To'] = to_email

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
    except Exception as e:
        # Log or raise the error for further handling
        print(f"Failed to send email to {to_email}: {e}")
        # Optionally raise error to let caller know
        # raise e
