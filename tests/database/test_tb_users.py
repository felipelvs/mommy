"""Run tests to ensure the application database is working properly."""

from sqlalchemy.exc import IntegrityError

from mommy.models import Month, Prototype, User

# * Where do Args come from
# app: The "app" fixture created on "conftest.py"
# config: The "pytest-flask" library automatically creates the fixture
# client: The "pytest-flask" library automatically creates the fixture


def test_db_is_clean(db):
    """Empty the database."""
    assert db.drop_all() is None


def test_db_is_created(db):
    """Mount the database."""
    assert db.create_all() is None


def test_user_table_is_clean():
    """Test if users table is empty."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user is None


def test_user_insert_without_email(db):
    """
    Test if the system generates an error with the insertion of a user without e-mail.
    """
    user = User(email="")
    user.set_password("correct_password")

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user is None


def test_user_insert_without_password(db):
    """
    Test if the system generates an error with the insertion of a user without password.
    """
    user = User(email="mommy@python.flask")

    error = False

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_valid_user_insert(db):
    """
    Test if the system does not generate an error with the insertion of a valid user.
    """
    user = User(email="mommy@python.flask")
    user.set_password("correct_password")

    db.session.add(user)
    db.session.commit()

    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user is not None


def test_user_insert_with_existent_email(db):
    """
    Test if the system generates an error with the insertion of a user with an existent
    e-mail.
    """
    user = User(email="mommy@python.flask")
    user.set_password("correct_password")

    error = False

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_user_insert_with_existent_password(db):
    """
    Test if the system does not generates an error with the insertion of a user with an
    existent password.
    """
    user = User(email="mommy2@python.flask")
    user.set_password("correct_password")

    error = False

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is False


def test_user_id_is_str():
    """Test if the user id is str."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert type(user.id) is str


def test_user_email_is_str():
    """Test if the user email is str."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert type(user.email) is str


def test_user_password_is_bytes():
    """Test if the user password is not int."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert type(user.password) is bytes


def test_user_received_entered_email():
    """Test if the user received the entered email."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user.email == "mommy@python.flask"


def test_user_correct_password_returns_true():
    """Test if the correct password generates a valid hash."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user.check_password("correct_password") is True


def test_user_incorrect_password_returns_false():
    """Test if the incorrect password generates a invalid hash."""
    user = User.query.filter_by(email="mommy@python.flask").first()

    assert user.check_password("incorrect_password") is False
