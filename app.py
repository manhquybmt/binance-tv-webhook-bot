from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {
        "service": "Binance TradingView Webhook Bot",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


if __name__ == "__main__":
    from config import HOST, PORT

    app.run(host=HOST, port=PORT)
