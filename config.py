import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SQLALCHEMY_DATABASE_URI = "sqlite:///data/trading.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
