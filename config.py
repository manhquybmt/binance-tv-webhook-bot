import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 5000))

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "CHANGE_ME")

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY", "")

TESTNET = os.getenv("TESTNET", "True").lower() == "true"
