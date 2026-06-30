from flask import Flask, request, jsonify
from config import HOST, PORT, WEBHOOK_SECRET

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
    return {"status": "ok"}


@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON"
        }), 400

    # Kiểm tra Secret
    if data.get("secret") != WEBHOOK_SECRET:
        return jsonify({
            "success": False,
            "message": "Invalid secret"
        }), 401

    print("=" * 50)
    print("TradingView Alert Received")
    print(data)
    print("=" * 50)

    return jsonify({
        "success": True,
        "message": "Webhook received"
    })


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
