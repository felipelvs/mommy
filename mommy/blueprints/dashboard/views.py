from flask import Blueprint, render_template

dashboard_bp = Blueprint(
    name="dashboard", import_name=__name__, url_prefix="/dashboard/"
)


@dashboard_bp.route("/")
def home():
    return render_template("dashboard/home.html")
