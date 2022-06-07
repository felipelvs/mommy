"""Authentication Blueprint and Routes."""

from blueprints.authentication.forms import SignUpForm
from flask import Blueprint, flash, render_template
from models import User, db

authentication_bp = Blueprint(
    name="authentication", import_name=__name__, url_prefix="/authentication/"
)


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
            flash(message="Account successfully created.", category="success")

    return render_template("authentication/sign_up.html", form=form)
