"""Run tests to ensure the application database is working properly."""

from datetime import datetime

from sqlalchemy.exc import IntegrityError

from mommy.models import Month, User

# * Where do Args come from
# app: The "app" fixture created on "conftest.py"
# config: The "pytest-flask" library automatically creates the fixture
# client: The "pytest-flask" library automatically creates the fixture


def test_month_insert_without_month_name(db):
    """
    Test if the system generates an error with the insertion of a month without month
    name.
    """
    # Get current date
    current_date = datetime.now()
    current_year = current_date.strftime("%Y")

    # Get user_id
    user = User.query.filter_by(email="admin@root.mommy").first()

    # Create month object
    month = Month(year=current_year, user_id=user.id)

    error = False
    try:
        db.session.add(month)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_month_insert_without_year(db):
    """
    Test if the system generates an error with the insertion of a month without year.
    """
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")

    # Get user_id
    user = User.query.filter_by(email="admin@root.mommy").first()

    # Create month object
    month = Month(month=current_month, user_id=user.id)

    error = False
    try:
        db.session.add(month)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_month_insert_without_user_id(db):
    """
    Test if the system generates an error with the insertion of a month without user's
    id.
    """
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    # Create month object
    month = Month(month=current_month, year=current_year)

    error = False
    try:
        db.session.add(month)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_valid_month_insert(db):
    """
    Test if the system does not generate an error with the insertion of a valid month.
    """
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    # Get user_id
    user = User.query.filter_by(email="admin@root.mommy").first()

    # Create month object
    month = Month(month=current_month, year=current_year, user_id=user.id)

    db.session.add(month)
    db.session.commit()

    month = Month.query.filter_by(
        month=current_month, year=current_year, user_id=user.id
    ).first()

    assert month is not None


def test_month_id_is_str():
    """Test if the month's id is str."""
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    month = Month.query.filter_by(month=current_month, year=current_year).first()

    assert type(month.id) is str


def test_month_name_is_str():
    """Test if the month's name is str."""
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    month = Month.query.filter_by(month=current_month, year=current_year).first()

    assert type(month.month) is str


def test_month_year_is_str():
    """Test if the month's year is str."""
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    month = Month.query.filter_by(month=current_month, year=current_year).first()

    assert type(month.year) is str


def test_month_user_id_is_str():
    """Test if the month's user_id is str."""
    # Get current date
    current_date = datetime.now()
    current_month = current_date.strftime("%b")
    current_year = current_date.strftime("%Y")

    month = Month.query.filter_by(month=current_month, year=current_year).first()

    assert type(month.user_id) is str
