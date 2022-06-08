"""Flask forms."""

from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class AddPrototypeForm(FlaskForm):
    """Add prototype WTForm."""

    name = StringField(
        label="name",
        validators=[
            DataRequired(message="This field cannot be empty."),
            Length(
                min=2,
                max=32,
                message="Must be between 1 and 32 characters.",
            ),
        ],
    )

    stones = IntegerField(
        label="stones",
        validators=[
            DataRequired(message="This field cannot be empty."),
            NumberRange(
                min=1,
                max=400,
                message="Must be between 1 and 400.",
            ),
        ],
    )

    made = IntegerField(
        label="made",
        validators=[
            DataRequired(message="This field cannot be empty."),
            NumberRange(
                min=1,
                max=300,
                message="Must be between 1 and 300.",
            ),
        ],
    )

    value = RadioField(
        label="value",
        validators=[
            DataRequired(message="Required selection."),
        ],
        choices=[
            ("0.025", "R$ 0,025"),
            ("0.040", "R$ 0,040"),
        ],
        validate_choice=True,
    )

    submit = SubmitField(label="Add")
