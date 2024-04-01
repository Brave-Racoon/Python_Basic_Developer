from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for, flash,
)
from werkzeug.exceptions import BadRequest

from models import Products, db
from . import crud


products_implement = Blueprint(
    "products_implement",
    __name__,
    url_prefix="/products",
)


@products_implement.get(
    "/",
    endpoint="list",
)
def get_products():
    return render_template(
        "products/list.html",
        products=crud.get_products(),
    )


@products_implement.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("product-name is required!")

    product_descr = request.form.get("product-descr", "")
    product_descr = product_descr.strip()
    if not product_descr:
        raise BadRequest("product-descr is required!")

    product_price = request.form.get("product-price", type=int)
    if not product_price:
        raise BadRequest("product-price is required!")

    product_discount = request.form.get("product-discount", type=float)
    if product_discount < 0:
        raise BadRequest("product-discountPercentage is required!")

    product_rating = request.form.get("product-rating", type=float)
    if product_rating < 0:
        raise BadRequest("product-rating is required!")

    product_stock = request.form.get("product-stock", type=int)
    if product_stock < 0:
        raise BadRequest("product-stock is required!")

    product_brand = request.form.get("product-brand", type=str)
    if not product_brand:
        raise BadRequest("product-brand is required!")

    product = crud.create_product(
        name=product_name,
        descr=product_descr,
        price=product_price,
        discount=product_discount,
        rating=product_rating,
        stock=product_stock,
        brand=product_brand,
    )

    flash(f"Created product {product_name!r}!", category="success")
    # return {"product": product.name, "id": product.id}
    url = url_for(
        "products_implement.details",
        product_id=product.id,
    )
    return redirect(url)


@products_implement.get(
    "/<int:product_id>/",
    endpoint="details",
)
def get_product_details(product_id: int):
    product: Products = Products.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    return render_template(
        "products/details.html",
        product=product,
    )


@products_implement.route(
    "/<int:product_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_product(product_id: int):
    product: Products = Products.query.get_or_404(
        product_id,
        description=f"Product #{product_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "products/delete.html",
            product=product,
        )

    product_name = product.title
    db.session.delete(product)
    db.session.commit()

    flash(f"Deleted {product_name!r} successfully!", category="warning")
    url = url_for("products_implement.list")
    return redirect(url)
