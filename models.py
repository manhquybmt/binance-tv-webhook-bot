from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    order_id = Column(String)

    symbol = Column(String)

    side = Column(String)

    qty = Column(Float)

    price = Column(Float)

    status = Column(String)

    pnl = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)
