"""Contains the database model using SQLAlchemy."""

from datetime import datetime
from uuid import uuid4

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def generate_uuid():
    return str(uuid4())


class User(db.Model, UserMixin):
    """Represents "tb_users" table."""

    __tablename__ = "tb_users"

    id = db.Column(
        db.String(36),
        nullable=False,
        primary_key=True,
        unique=True,
        default=generate_uuid,
    )
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def set_password(self, password: str):
        """Hash the user's password."""
        self.password = generate_password_hash(password)

    def check_password(self, password: str):
        """Check if the password matches the hash."""
        return check_password_hash(pw_hash=self.password, password=password)


class Month(db.Model):
    """Represents "tb_months" table."""

    __tablename__ = "tb_months"

    id = db.Column(
        db.String(36),
        nullable=False,
        primary_key=True,
        unique=True,
        default=generate_uuid,
    )
    month = db.Column(db.String(3), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("tb_users.id"), nullable=False)


class Prototype(db.Model):
    """Represents "tb_prototypes" table."""

    __tablename__ = "tb_prototypes"

    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    stones = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    prototypes_made = db.Column(db.Integer, nullable=False)
    stones_made = db.Column(db.Integer, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("tb_users.id"), nullable=False)
    month_id = db.Column(db.String(36), db.ForeignKey("tb_months.id"), nullable=False)
