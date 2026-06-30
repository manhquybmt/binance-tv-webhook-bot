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
    return {"status": "ok"}


@app.post("/webhook")
symbol = data.get("symbol")
side = data.get("side")
qty = data.get("qty")

# Kiểm tra dữ liệu
if side not in ("BUY", "SELL"):
    return jsonify({
        "success": False,
        "message": "Invalid side"
    }), 400

if not symbol:
    return jsonify({
        "success": False,
        "message": "Missing symbol"
    }), 400

if qty is None or float(qty) <= 0:
    return jsonify({
        "success": False,
        "message": "Invalid quantity"
    }), 400

try:
    order = place_market_order(
        symbol=symbol,
        side=side,
        quantity=qty
    )

    return jsonify({
        "success": True,
        "orderId": order["orderId"],
        "status": order["status"]
    })

except Exception as e:
    return jsonify({
        "success": False,
        "message": str(e)
    }), 500

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
