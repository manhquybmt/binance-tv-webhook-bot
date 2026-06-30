from binance.um_futures import UMFutures

from config import (
    BINANCE_API_KEY,
    BINANCE_SECRET_KEY,
    TESTNET,
)

BASE_URL = (
    "https://testnet.binancefuture.com"
    if TESTNET
    else "https://fapi.binance.com"
)

client = UMFutures(
    key=BINANCE_API_KEY,
    secret=BINANCE_SECRET_KEY,
    base_url=BASE_URL,
)


def place_market_order(symbol, side, quantity):
    return client.new_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )
