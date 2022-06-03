"""Main blueprint."""


from flask import Blueprint

main_bp = Blueprint(name="main", import_name=__name__, url_prefix="/")


@main_bp.route("/")
def index():
    return "I'm Mommy; an application made for Felipe's mom."
