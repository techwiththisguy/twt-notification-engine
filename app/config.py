import os
from dotenv import load_dotenv

load_dotenv()

def env(key: str, default: str = "") -> str:
    return os.getenv(key, default)

APP_NAME = env("APP_NAME", "TWT Notification Engine")
ENV = env("ENV", "dev")

SMTP_HOST = env("SMTP_HOST")
SMTP_PORT = int(env("SMTP_PORT", "587"))
SMTP_USERNAME = env("SMTP_USERNAME")
SMTP_PASSWORD = env("SMTP_PASSWORD")
SMTP_FROM = env("SMTP_FROM")

DEFAUL_NOTIFY_EMAIL = env("DEFAULT_NOTIFY_EMAIL")
FORWARD_WEBHOOK_URL = env("FORWARD_WEBHOOK_URL")