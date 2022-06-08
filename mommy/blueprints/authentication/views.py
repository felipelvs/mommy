"""Authentication Blueprint and Routes."""

from datetime import datetime

from blueprints.authentication.forms import SignInForm, SignUpForm
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_user
from models import Month, User, db

authentication_bp = Blueprint(
    name="authentication", import_name=__name__, url_prefix="/authentication/"
)

login_manager = LoginManager()


@login_manager.user_loader
def load_user(id: str):
    """
    Reload the user object from the user ID stored in the session.

    Args:
        id (str): user id

    Returns:
        Returns the user object if the id is valid, if the id is invalid
        returns None.
    """
    return User.query.get(id)


def init_first_month(user_id: str):
    """Initialize the user's first month if there is no month in tb_months."""
    month = Month.query.filter_by(user_id=user_id).first()

    if month:
        return False

    now = datetime.now()
    current_month = now.strftime("%b")
    current_year = now.strftime("%Y")

    month = Month(
        month=current_month,
        year=current_year,
        user_id=user_id,
    )

    db.session.add(month)
    db.session.commit()

    return True


@authentication_bp.route("/sign_up/", methods=["GET", "POST"])
def sign_up():
    """
    Render the sign up page.

    If the route is accessed with the POST method, register a user.
    """
    form = SignUpForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash(message="This email address is already being used.", category="error")
        else:
            user = User(email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            user = User.query.filter_by(email=form.email.data).first()
            init_first_month(user.id)

            flash(message="Account successfully created.", category="success")
            return redirect(url_for("authentication.sign_in"))

    return render_template("authentication/sign_up.html", form=form)


@authentication_bp.route("/sign_in/", methods=["GET", "POST"])
def sign_in():
    """
    Render the sign in page.

    If the route is accessed with the POST method, auth a user.
    """
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("dashboard.home"))
        else:
            flash(message="Incorrect email address or password.", category="error")

    return render_template("authentication/sign_in.html", form=form)
