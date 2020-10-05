import logging
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from app.config import config


# set up flask-sqlalchemy
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/
db = SQLAlchemy()


# set up rest-x
# https://flask-restx.readthedocs.io/en/latest/quickstart.html
authorizations = {"basic_auth": {"type": "basic"}}
restx = Api(
    version="1.0",
    title="Ross Mountjoy Portfolio API",
    description="Get info from Ross Mountjoy's portfolio",
    authorizations=authorizations,
    prefix="/api/",
    doc="/api/",
)


# Lazily initialize the flask extensions
def register_extensions(app):
    db.init_app(app)
    restx.init_app(app)


# register the blueprint modules
def register_blueprints(app):
    from app.api import api

    app.register_blueprint(api, url_prefix="/api")

    from app.site import site

    app.register_blueprint(site)


# set up the database
def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config_name):
    """
    Factory to create Flask application context using config option found in
    app.config

    :param config_name: (string) name of the chosen config option
    :return app: (Flask application context)
    """
    logging.basicConfig(
        filename="app.log",
        filemode="w",
        format="%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    logging.info("App initialized.")
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)

    return app
