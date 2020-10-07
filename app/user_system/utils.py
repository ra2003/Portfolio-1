from app import db, bcrypt
from .models import User


def create_user(username, password, role):
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password=hashed_password, role=role)
    db.session.add(user)
    db.session.commit()


def change_password(user_id, new_password):
    user = User.query.filter_by(id=user_id).first()
    hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")
    user.password = hashed_password
    db.session.merge(user)
    db.session.commit()
