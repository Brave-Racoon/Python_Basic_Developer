"""
Create
Read
Update
Delete
"""

import requests
from sqlalchemy import select, func, create_engine
from sqlalchemy.orm import sessionmaker

from models import db, Products
from config import PRODUCTS_DATA_URL, SQLALCHEMY_DATABASE_URI


def drop_database():
    db.metadata.drop_all()


def create_database():
    db.metadata.create_all()


def create_product(name: str, descr: str, price: int, discount: float, rating: float, stock: int, brand: str) -> Products:
    last_id = db.session.query(func.max(Products.id)).scalar()
    if last_id is None:
        last_id = 0
    product = Products(title=name, description=descr, price=price, discountPercentage=discount,rating=rating, stock=stock, brand=brand, id=last_id+1)
    db.session.add(product)
    db.session.commit()
    return product


def get_products() -> list[Products]:
    mylist = list(db.session.scalars(select(Products)).all())
    return mylist


def fetch_api(url: str) -> dict:
    response = requests.get(url)
    data = response.json()
    return data


def count_rows(sess, table_class):
    return sess.query(func.count(table_class.id)).scalar()


def fill_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    id_counter = db.session.query(func.count(Products.id)).scalar()
    if not id_counter:
        products_data = fetch_api(PRODUCTS_DATA_URL)
        for item in products_data['products']:
            product = Products(id=item['id'], title=item['title'], description=item['description'], price=item['price'],
                               discountPercentage=item['discountPercentage'], rating=item['rating'],
                               stock=item['stock'], brand=item['brand'])
            session.add(product)
        session.commit()
        print('Fetched rows: ', count_rows(session, Products))
    else: print("Db doesn't empty.")
    session.close()
