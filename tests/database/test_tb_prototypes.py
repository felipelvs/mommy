"""Run tests to ensure the application database is working properly."""

from sqlalchemy.exc import IntegrityError

from mommy.models import Month, Prototype, User

# * Where do Args come from
# app: The "app" fixture created on "conftest.py"
# config: The "pytest-flask" library automatically creates the fixture
# client: The "pytest-flask" library automatically creates the fixture


def test_prototype_insert_without_name(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    name.
    """
    prototype = Prototype(stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_stones(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    stones.
    """
    prototype = Prototype(name="Star", value=0.025, prototypes_made=76)
    prototype.stones_made = 100
    prototype.profit = 100

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_value(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    value.
    """
    prototype = Prototype(name="Star", stones=134, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * 0.025

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_prototypes_made(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    prototypes_made.
    """
    prototype = Prototype(name="Star", stones=134, value=0.025)
    prototype.stones_made = prototype.stones * 76
    prototype.profit = prototype.stones_made * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_stones_made(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    stones_made.
    """
    prototype = Prototype(name="Star", stones=134, value=0.025, prototypes_made=76)
    prototype.profit = 10184 * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_profit(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    profit.
    """
    prototype = Prototype(stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_user_id(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    user_id.
    """
    prototype = Prototype(stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.month_id = last_month.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_prototype_insert_without_month_id(db):
    """
    Test if the system generates an error with the insertion of a prototype without
    month_id.
    """
    prototype = Prototype(stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()

    prototype.user_id = user.id

    error = False
    try:
        db.session.add(prototype)
        db.session.commit()
    except IntegrityError:
        error = True

    assert error is True


def test_valid_prototype_insert(db):
    """
    Test if the system does not generate an error with the insertion of a valid
    prototype.
    """
    prototype = Prototype(name="Star", stones=134, value=0.025, prototypes_made=76)
    prototype.stones_made = prototype.stones * prototype.prototypes_made
    prototype.profit = prototype.stones_made * prototype.value

    user = User.query.filter_by(email="admin@root.mommy").first()
    months = Month.query.filter_by(user_id=user.id).all()
    last_month = months[-1]

    prototype.user_id = user.id
    prototype.month_id = last_month.id

    db.session.add(prototype)
    db.session.commit()

    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert prototype is not None


def test_prototype_id_is_int():
    """Test if the prototype's id is int."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.id) is int


def test_prototype_name_is_str():
    """Test if the prototype's name is str."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.name) is str


def test_prototype_stones_is_int():
    """Test if the prototype's stones is int."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.stones) is int


def test_prototype_value_is_float():
    """Test if the prototype's value is float."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.value) is float


def test_prototype_prototypes_made_is_int():
    """Test if the prototype's prototypes_made is int."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.prototypes_made) is int


def test_prototype_stones_made_is_int():
    """Test if the prototype's stones_made is int."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.stones_made) is int


def test_prototype_profit_is_float():
    """Test if the prototype's profit is float."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.profit) is float


def test_prototype_user_id_is_str():
    """Test if the prototype's user_id is str."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.user_id) is str


def test_prototype_month_id_is_str():
    """Test if the prototype's month_id is str."""
    prototype = Prototype.query.filter_by(
        name="Star", stones=134, value=0.025, prototypes_made=76
    ).first()

    assert type(prototype.month_id) is str
