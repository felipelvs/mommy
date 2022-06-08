from flask import Blueprint, render_template
from flask_login import login_required

dashboard_bp = Blueprint(
    name="dashboard", import_name=__name__, url_prefix="/dashboard/"
)


@dashboard_bp.route("/")
@login_required
def home():
    return render_template("dashboard/home.html")
