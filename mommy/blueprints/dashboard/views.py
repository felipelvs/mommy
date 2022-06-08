from locale import LC_MONETARY, currency, setlocale

from flask import Blueprint, render_template
from flask_login import current_user, login_required
from models import Month, Prototype

dashboard_bp = Blueprint(
    name="dashboard", import_name=__name__, url_prefix="/dashboard/"
)


def translate_currency_to_br(currency_value: float):
    """Translate a float value to be displayed in Brazilian currency."""
    setlocale(LC_MONETARY, "pt_BR.UTF-8")

    return currency(currency_value)


def get_month_summary(month_id: str):
    """Get the summary of the month."""
    month_name = ""
    prototypes_made = 0
    stones_made = 0
    profit = 0.0

    month = Month.query.filter_by(id=month_id).first()
    if not month:
        return False

    prototypes = Prototype.query.filter_by(month_id=month_id)
    if prototypes:
        for prototype in prototypes:
            prototypes_made += prototype.prototypes_made
            stones_made += prototype.stones_made
            profit += prototype.profit

    month_name = month.month

    return {
        "month": month_name,
        "prototypes_made": prototypes_made,
        "stones_made": stones_made,
        "profit": translate_currency_to_br(profit),
    }


def get_current_month_id(user_id: str):
    """Get current month id."""
    months = Month.query.filter_by(user_id=user_id).all()
    last_month = months[-1]

    return last_month.id


@dashboard_bp.route("/")
@login_required
def home():
    summary = get_month_summary(
        month_id=get_current_month_id(current_user.id),
    )

    return render_template("dashboard/home.html", summary=summary)
