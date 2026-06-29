from database import SessionLocal
from models import Order


@app.route("/api/orders")
def orders():

    db = SessionLocal()

    data = db.query(Order).order_by(Order.id.desc()).limit(100).all()

    result = []

    for i in data:

        result.append({
            "id": i.id,
            "symbol": i.symbol,
            "side": i.side,
            "qty": i.qty,
            "price": i.price,
            "status": i.status,
            "time": i.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    db.close()

    return result
