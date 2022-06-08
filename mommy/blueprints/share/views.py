from blueprints.dashboard.views import get_month_details, get_month_summary
from flask import Blueprint, render_template
from models import Month

share_bp = Blueprint(name="share", import_name=__name__, url_prefix="/share/")


def get_closed_months(user_id: str):
    months = Month.query.filter_by(user_id=user_id).all()

    return months


@share_bp.route("/<user_id>")
def list_closed_months(user_id: str):
    closed_months = get_closed_months(user_id)

    return render_template("share/list.html", closed_months=closed_months)


@share_bp.route("/month/<month_id>")
def get_month(month_id: int):
    summary = get_month_summary(
        month_id=month_id,
    )

    details = get_month_details(
        month_id=month_id,
    )

    return render_template("share/month.html", summary=summary, details=details)
