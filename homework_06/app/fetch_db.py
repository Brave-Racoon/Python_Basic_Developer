from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import config
from models import db, Products
from views.products.crud import fetch_api, count_rows


def fill_db():
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    id_counter = db.session.query(func.count(Products.id)).scalar()
    if not id_counter:
        products_data = fetch_api(config.PRODUCTS_DATA_URL)
        for item in products_data['products']:
            product = Products(id=item['id'], title=item['title'], description=item['description'],
                               price=item['price'],
                               discountPercentage=item['discountPercentage'], rating=item['rating'],
                               stock=item['stock'], brand=item['brand'])
            session.add(product)
        session.commit()
        print('Fetched rows: ', count_rows(session, Products))
    else:
        print("Db doesn't empty.")

    session.close()

