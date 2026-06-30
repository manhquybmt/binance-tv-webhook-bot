from flask import Flask, request, jsonify

from config import HOST, PORT, WEBHOOK_SECRET
from binance_api import place_market_order

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


@app.post("/webhook")
def webhook():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Invalid JSON"
        }), 400

    # Verify webhook secret
    if data.get("secret") != WEBHOOK_SECRET:
        return jsonify({
            "success": False,
            "message": "Invalid secret"
        }), 401

    symbol = data.get("symbol")
    side = str(data.get("side", "")).upper()
    qty = data.get("qty")

    # Validate data
    if not symbol:
        return jsonify({
            "success": False,
            "message": "Missing symbol"
        }), 400

    if side not in ["BUY", "SELL"]:
        return jsonify({
            "success": False,
            "message": "Invalid side"
        }), 400

    try:
        qty = float(qty)

        if qty <= 0:
            raise ValueError()

    except Exception:
        return jsonify({
            "success": False,
            "message": "Invalid quantity"
        }), 400

    print("=" * 60)
    print("TradingView Alert")
    print(data)
    print("=" * 60)

    try:

        order = place_market_order(
            symbol=symbol,
            side=side,
            quantity=qty
        )

        return jsonify({
            "success": True,
            "message": "Order placed",
            "order": order
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT
    )
