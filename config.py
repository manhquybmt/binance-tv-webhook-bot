import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME", "Binance TV Webhook Bot")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")

    DATABASE = os.getenv("DATABASE", "database/bot.db")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")