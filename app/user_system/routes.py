from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app import db, login_manager, bcrypt
from . import user_system
from .models import User
from .utils import create_user


@user_system.before_app_first_request
def add_default_user():
    # create default user
    if not User.query.first():
        create_user(username="admin", password="admin", role="admin")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@user_system.route("/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))
    return render_template("user_system/login.html")


@user_system.route("/check_login", methods=["POST"])
def check_login():
    username = request.form.get("username")
    password = request.form.get("password")
    remember = request.form.get("remember")

    user = User.query.filter_by(username=username).first()
    if not user:
        return "User not found"
    if bcrypt.check_password_hash(user.password, password):
        login_user(user, remember=remember)
    else:
        return "Password is wrong"
    return "success"


@user_system.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("user_system.login"))
