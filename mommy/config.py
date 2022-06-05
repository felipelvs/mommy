"""Creates the settings that the app can use."""


class Config(object):
    TESTING = False


class ProductionConfig(Config):
    """Configuration used for production."""

    DEBUG = False

    SECRET_KEY = ""

    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configuration used for development."""

    DEBUG = True

    SECRET_KEY = "c0cf0dc51db2a9d5eb29e79e28f3b72f"

    SQLALCHEMY_DATABASE_URI = "sqlite:///database-dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Configuration used for testing."""

    DEBUG = False
    TESTING = True

    SECRET_KEY = "18f59a8d425e7c3e0f17755e1f274c3c"

    SQLALCHEMY_DATABASE_URI = "sqlite:///../tests/database-tests.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
