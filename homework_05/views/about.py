from flask import Blueprint

about_view = Blueprint(
    "About",
    __name__,
    url_prefix="about",
)
