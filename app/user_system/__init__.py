from flask import Blueprint

user_system = Blueprint("user_system", __name__)

from . import models, routes
