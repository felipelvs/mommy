from datetime import datetime
from locale import LC_MONETARY, currency, setlocale

from blueprints.dashboard.forms import AddPrototypeForm
from dateutil import relativedelta
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from models import Month, Prototype, db

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


def get_month_details(month_id: str):
    """Get the details of all prototypes added in the month."""
    prototypes = Prototype.query.filter_by(month_id=month_id).all()

    if prototypes:
        for prototype in prototypes:
            prototype.date = prototype.date.strftime("%d/%m/%Y")
            prototype.value = "R$ {v}".format(
                v=prototype.value,
            ).replace(".", ",")
            prototype.profit = translate_currency_to_br(prototype.profit)

    return prototypes


def get_current_month_name(user_id: str):
    """Get current month name."""
    months = Month.query.filter_by(user_id=user_id).all()
    last_month = months[-1]
    return last_month.month


def get_current_month_year(user_id: str):
    """Get current month year."""
    months = Month.query.filter_by(user_id=user_id).all()
    last_month = months[-1]
    return last_month.year


def close_month_db():
    date = datetime.now()
    month = date.strftime("%b")
    next_month = date.today() + relativedelta.relativedelta(months=1)

    db_month = get_current_month_name(current_user.id)
    if db_month == next_month.strftime("%b"):
        return False

    if date.day > 5:
        month = next_month.strftime("%b")

    new_month = Month(
        month=month,
        year=date.year,
        user_id=current_user.id,
    )
    db.session.add(new_month)
    db.session.commit()

    return True


@dashboard_bp.route("/")
@login_required
def home():
    summary = get_month_summary(
        month_id=get_current_month_id(current_user.id),
    )

    details = get_month_details(
        month_id=get_current_month_id(current_user.id),
    )

    return render_template("dashboard/home.html", summary=summary, details=details)


@dashboard_bp.route("/add_prototype/", methods=["GET", "POST"])
@login_required
def add_prototype():
    form = AddPrototypeForm()
    if form.validate_on_submit():
        prototype = Prototype(
            name=form.name.data,
            stones=form.stones.data,
            value=float(form.value.data),
            prototypes_made=form.made.data,
        )
        prototype.stones_made = prototype.stones * prototype.prototypes_made
        prototype.profit = prototype.stones_made * prototype.value
        prototype.user_id = current_user.id
        prototype.month_id = get_current_month_id(current_user.id)

        db.session.add(prototype)
        db.session.commit()

        flash(message="Prototype successfully added.", category="success")
        return redirect(url_for("dashboard.home"))

    return render_template("dashboard/add.html", form=form)


@dashboard_bp.route(
    "/remove_prototype/<int:prototype_id>/<ask>", methods=["GET", "POST"]
)
@login_required
def remove_prototype(prototype_id: int, ask: str = "Yes"):
    prototype = Prototype.query.filter_by(id=prototype_id).first()

    if not prototype:
        flash(message="Prototype not found on system.", category="error")
        return redirect(url_for("dashboard.home"))

    if prototype and ask == "No":
        db.session.delete(prototype)
        db.session.commit()
        return redirect(url_for("dashboard.home"))

    return render_template("dashboard/remove.html", prototype=prototype)


@dashboard_bp.route(
    "/close_month/<ask>",
    methods=["GET"],
)
@login_required
def close_month(ask: str = "Yes"):
    current_month = get_current_month_name(current_user.id)
    current_year = get_current_month_year(current_user.id)

    if ask == "No":
        if close_month_db():
            return redirect(url_for("dashboard.home"))
        else:
            flash(message="Unable to close the month.", category="error")

        return redirect(url_for("dashboard.home"))

    return render_template(
        "dashboard/close.html",
        current_month=current_month,
        current_year=current_year,
    )
