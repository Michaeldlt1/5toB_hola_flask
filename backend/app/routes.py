from flask import Blueprint, flash, redirect, render_template, request, url_for

from .services import UserService

main_bp = Blueprint("main", __name__)


def get_user_service(app):
    if "user_service" not in app.config:
        app.config["user_service"] = UserService(app.config.get("USERS", []))
    return app.config["user_service"]


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/health")
def health():
    return {"status": "ok"}


@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("Completa todos los campos", "error")
            return render_template("register.html")

        service = get_user_service(current_app)
        service.create_user(name, email, password)
        flash("Registro exitoso", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("register.html")


@main_bp.route("/dashboard")
def dashboard():
    service = get_user_service(current_app)
    users = service.list_users()
    return render_template("dashboard.html", users=users)
