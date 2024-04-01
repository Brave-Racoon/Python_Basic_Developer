from sqlalchemy import String, Integer, Float

from sqlalchemy.orm import Mapped, mapped_column

from models.db import db


class Products(db.Model):
    title: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    discountPercentage: Mapped[float] = mapped_column(Float)
    rating: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)
    brand: Mapped[str] = mapped_column(String(255))

