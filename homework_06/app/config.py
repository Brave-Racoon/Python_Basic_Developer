import os

PRODUCTS_DATA_URL = "https://dummyjson.com/products"
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    "postgresql+psycopg://user:example@localhost:5432/products",
)
SQLALCHEMY_ECHO = False
