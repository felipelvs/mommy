"""Main blueprint."""


from flask import Blueprint, redirect, url_for

main_bp = Blueprint(name="main", import_name=__name__, url_prefix="/")


@main_bp.route("/")
def index():
    return redirect(url_for("authentication.sign_in"))
