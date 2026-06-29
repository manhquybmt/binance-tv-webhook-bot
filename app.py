from flask import Flask, request, jsonify
from binance_bot import execute_order
import os

app = Flask(__name__)

SECRET=os.getenv("WEBHOOK_SECRET")


@app.route('/webhook', methods=['POST'])
def webhook():

    data=request.json

    if data.get("secret") != SECRET:
        return jsonify({"error":"unauthorized"}),401


    result=execute_order(data)

    return jsonify(result)



@app.route('/')
def home():
    return "Trading Bot Running"


if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
