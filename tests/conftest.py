"""Prepare the test environment so that it works correctly."""

import pytest
from flask_sqlalchemy import SQLAlchemy

from mommy.app import Flask, create_app
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

    return mommy_db
