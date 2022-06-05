"""Perform tests to ensure the app and main blueprint are running correctly."""

# * Where do Args come from
# app: The "app" fixture created on "conftest.py"
# config: The "pytest-flask" library automatically creates the fixture
# client: The "pytest-flask" library automatically creates the fixture


def test_app_is_created(app):
    """Test if the app was created."""
    assert app.name == "mommy.app"


def test_config_debug_is_false(config):
    """Test if the app is not using the DEBUG configuration."""
    assert config["DEBUG"] is False


def test_config_testing_is_true(config):
    """Tes if the app is using the TESTING configuration."""
    assert config["TESTING"] is True


def test_index_route_returns_ok(client):
    """Test whether the home route returns HTTP status 200 OK."""
    assert client.get("/").status_code == 200


def test_inexistent_route_returns_not_found(client):
    """Test if a non-existing route returns HTTP status 404 Not Found."""
    assert client.get("/im/a/inexistent/route/").status_code == 404
