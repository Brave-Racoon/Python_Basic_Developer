from flask import Blueprint

index_view = Blueprint(
    "Index",
    __name__,
    url_prefix="index",
)
