import smtplib
from email.mime.text import MIMEText

def send_verification_email(to_email: str, token: str):
    verification_link = f"http://localhost:8000/verify-email?token={token}"
    body = f"Please verify your email by clicking this link: {verification_link}"

    msg = MIMEText(body)
    msg['Subject'] = "Verify your email"
    msg['From'] = "your_email@example.com"
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')  # Replace with real credentials
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
