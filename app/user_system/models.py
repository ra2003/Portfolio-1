from datetime import datetime
from flask import url_for, redirect
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView
from app import db, admin, bcrypt


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(60))


class UserView(ModelView):
    column_exclude_list = ["password"]
    can_edit = False
    can_delete = False

    def on_model_change(self, form, model, is_created):
        hashed_password = bcrypt.generate_password_hash(model.password).decode("utf-8")
        model.password = hashed_password

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("user_system.login"))


admin.add_view(UserView(User, db.session))


class TestModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    test_string = db.Column(db.String(256))
    test_int = db.Column(db.Integer)
    test_date = db.Column(db.DateTime, default=datetime.utcnow())
    test_bool = db.Column(db.Boolean)


class TestModelView(ModelView):
    column_filters = [
        "id",
        "test_string",
        "test_int",
        "test_date",
        "test_bool",
    ]
    column_searchable_list = [
        "id",
        "test_string",
        "test_int",
        "test_date",
        "test_bool",
    ]

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("user_system.login"))


admin.add_view(TestModelView(TestModel, db.session))
