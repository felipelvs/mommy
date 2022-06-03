"""Prepare the test environment so that it works correctly."""

import pytest

from mommy.app import Flask, create_app


@pytest.fixture(scope="module")
def app() -> Flask:
    """
    Ensures that all tests will have the app.

    The scope="module" guarantees that tests will use the same app for all functions.
    """
    app = create_app()
    app.config.from_object("mommy.config.TestingConfig")

    return app
