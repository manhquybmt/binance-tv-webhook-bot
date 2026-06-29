from database import SessionLocal
from models import Order
from binance_bot import execute_order


def execute_signal(data):

    result = execute_order(data)

    db = SessionLocal()

    order = Order(
        order_id=result["orderId"],
        symbol=result["symbol"],
        side=result["side"],
        qty=float(result["origQty"]),
        price=float(result.get("avgPrice", 0) or 0),
        status=result["status"],
    )

    db.add(order)

    db.commit()

    db.close()

    return result
