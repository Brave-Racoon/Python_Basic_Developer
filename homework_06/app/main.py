# https://dummyjson.com/docs/products
# https://github.com/tiangolo/uwsgi-nginx-flask-docker

from flask import Flask, render_template
from flask_migrate import Migrate
import config
from models import db
from views.items import items_app
from views.products import products_implement
import fetch_db

app = Flask(__name__)


app.config.update(
    SECRET_KEY="6fc01f2db60feff0f535370",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

app.register_blueprint(items_app)
app.register_blueprint(products_implement)

db.init_app(app)
migrate = Migrate(app, db)



@app.get("/", endpoint="index")
def index():
    fetch_db.fill_db()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
