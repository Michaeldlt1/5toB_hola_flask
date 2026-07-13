import os

from flask import Flask

from .database import DatabaseUserService
from .routes import main_bp


def create_app() -> Flask:
    app = Flask(__name__, template_folder="../../frontend/templates", static_folder="../../frontend/static")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["USERS"] = []
    app.config["user_service"] = DatabaseUserService(app.config["USERS"])

    app.register_blueprint(main_bp)
    return app
