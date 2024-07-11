import os
from os import getenv
# from dotenv import load_dotenv

# load_dotenv("config.env")


class Telegram:
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    PORT = int(os.environ.get("PORT", 8080))
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
    BASE_URL = os.environ.get("BASE_URL").rstrip('/')
    DATABASE_URL = os.environ.get("DATABASE_URL")
    AUTH_CHANNEL = [channel.strip() for channel in os.environ.get("AUTH_CHANNEL").split(",")]
    THEME = os.environ.get("THEME", "quartz").lower()
    USERNAME = os.environ.get("USERNAME", "admin")
    PASSWORD = os.environ.get("PASSWORD", "admin")
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(os.environ.get('SLEEP_THRESHOLD', '60'))
    WORKERS = int(os.environ.get('WORKERS', '10'))
    MULTI_CLIENT = bool(os.environ.get('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(os.environ.get('HIDE_CHANNEL', 'False'))