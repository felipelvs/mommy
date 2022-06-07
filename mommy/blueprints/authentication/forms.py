"""Flask forms."""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignUpForm(FlaskForm):
    """User sign up WTForm."""

    email = StringField(
        label="email",
        validators=[
            DataRequired(message="This field cannot be empty."),
            Email(message="Enter a valid email address."),
            Length(
                min=6,
                max=254,
                message="Email must be between 6 and 254 characters.",
            ),
        ],
    )

    password = PasswordField(
        label="password",
        validators=[
            DataRequired(message="This field cannot be empty."),
            Length(
                min=8,
                max=38,
                message="Password must be between 8 and 38 characters.",
            ),
        ],
    )

    confirm_password = PasswordField(
        label="confirm_password",
        validators=[
            DataRequired(message="This field cannot be empty."),
            EqualTo(fieldname="password", message="Passwords don't match."),
            Length(
                min=8,
                max=38,
                message="Password must be between 8 and 38 characters.",
            ),
        ],
    )

    submit = SubmitField(label="Sign Up")


class SignInForm(FlaskForm):
    """User sign in WTForm."""

    email = StringField(
        label="email",
        validators=[
            DataRequired(message="This field cannot be empty."),
            Email(message="Enter a valid email address."),
            Length(
                min=6,
                max=254,
                message="Email must be between 6 and 254 characters.",
            ),
        ],
    )

    password = PasswordField(
        label="password",
        validators=[
            DataRequired(message="This field cannot be empty."),
            Length(
                min=8,
                max=38,
                message="Password must be between 8 and 38 characters.",
            ),
        ],
    )

    submit = SubmitField(label="Sign In")
