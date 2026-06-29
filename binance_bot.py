from binance.client import Client
import os


client=Client(
    os.getenv("BINANCE_KEY"),
    os.getenv("BINANCE_SECRET")
    symbol=SYMBOL,
    leverage=int(os.getenv("LEVERAGE",5))
)


SYMBOL=os.getenv("SYMBOL")
QTY=float(os.getenv("QTY"))



def execute_order(data):

    action=data["action"]


    if action=="LONG":

        order=client.futures_create_order(
            symbol=SYMBOL,
            side="BUY",
            type="MARKET",
            quantity=QTY
        )


    elif action=="SHORT":

        order=client.futures_create_order(
            symbol=SYMBOL,
            side="SELL",
            type="MARKET",
            quantity=QTY
        )


    elif action=="CLOSE":

        order=client.futures_create_order(
            symbol=SYMBOL,
            side="SELL",
            type="MARKET",
            quantity=QTY,
            reduceOnly=True
        )


    return order
