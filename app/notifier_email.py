import smtplib
from email.message import EmailMessage
from app import config
from app.store import log_delivery

def send_email(subject: str, body: str, to_email: str | None = None) -> None:
    to_email = to_email or config.DEFAULT_NOTIFY_EMAIL
    
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config.SMTP_FROM
    msg["To"] = to_email
    msg.set_content(body)
    
    try:
        with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            server.send_message(msg)
            
        log_delivery({"channel": "email", "to": to_email, "status": "sent", "subject": subject})
    except Exception as e:
        log_delivery({"channel": "email", "to": to_email, "status": "failed", "error": str(e), "subject": subject})
        raise