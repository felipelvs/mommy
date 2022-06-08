"""
Prepares the application to run.

If the file is opened for execution, it runs the application.
"""


from blueprints.authentication.views import authentication_bp, login_manager
from blueprints.dashboard.views import dashboard_bp
from flask import Flask
from models import db
from views import main_bp


def create_app():
    """Creates and configures the Flask instance."""
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    app.register_blueprint(main_bp)
    app.register_blueprint(authentication_bp)
    app.register_blueprint(dashboard_bp)

    db.app = app
    db.init_app(app)

    login_manager.init_app(app)

    return app


if __name__ == "__main__":
    mommy = create_app()
    mommy.run()
