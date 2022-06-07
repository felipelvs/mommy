"""Prepare the test environment so that it works correctly."""

import pytest
from flask_sqlalchemy import SQLAlchemy

from mommy.app import Flask, create_app
from mommy.models import Month, Prototype, User
from mommy.models import db as mommy_db


@pytest.fixture(scope="module")
def app() -> Flask:
    """
    Ensures that all tests will have the app.

    The scope="module" guarantees that tests will use the same app for all functions.
    """
    app = create_app()
    app.config.from_object("mommy.config.TestingConfig")

    return app


@pytest.fixture(scope="module")
def db(app) -> SQLAlchemy:
    """
    Ensures that all tests will have the database.

    The scope="module" guarantees that tests will use the same db for all functions.
    """
    mommy_db.app = app
    mommy_db.init_app(app)

    mommy_db.drop_all()
    mommy_db.create_all()

    # Insert user
    user = User(email="admin@root.mommy")
    user.set_password("correct_password")
    mommy_db.session.add(user)
    mommy_db.session.commit()

    # Insert month
    user = User.query.filter_by(email="admin@root.mommy").first()
    month = Month(month="Jun", year="2022", user_id=user.id)
    mommy_db.session.add(month)
    mommy_db.session.commit()

    # Insert a prototype
    prototype = Prototype(name="Star", stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * prototype.value
    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]
    prototype.user_id = user.id
    prototype.month_id = last_month.id
    mommy_db.session.add(prototype)
    mommy_db.session.commit()

    return mommy_db
