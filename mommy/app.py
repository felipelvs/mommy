"""
Prepares the application to run.

If the file is opened for execution, it runs the application.
"""


from flask import Flask
from views import main_bp


def create_app():
    """Creates and configures the Flask instance."""
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    app.register_blueprint(main_bp)

    return app


if __name__ == "__main__":
    mommy = create_app()
    mommy.run()
