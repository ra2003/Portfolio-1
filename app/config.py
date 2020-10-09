# This is the configuration file for the Flask app. Go here for options:
# https://flask.palletsprojects.com/en/1.1.x/config/

# before you start the server, set the CONFIG env variable to select one of these
# options: default, dev, prod, test
# example:
# export CONFIG=dev

# This would obviously need to be pulled in from a credentials manager
# I have left this here if you would like to test it out yourself.
AWS_DATABASE_URI = (
    "mysql+mysqlconnector://admin:8vxSQCSL2VVNvb@portfolio."
    "ckwxpbebwiuv.us-east-2.rds.amazonaws.com/portfolio"
)
# same here
SECRET_KEY = "80268a09e0244202a4c0fb7f2c26f4cd"


FLASK_ADMIN_SWATCH = "darkly"

SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 280, "pool_size": 100}


class Config:
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = AWS_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY
    FLASK_ADMIN_SWATCH = FLASK_ADMIN_SWATCH
    SQLALCHEMY_ENGINE_OPTIONS = SQLALCHEMY_ENGINE_OPTIONS


class TestingConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = AWS_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY
    FLASK_ADMIN_SWATCH = FLASK_ADMIN_SWATCH
    SQLALCHEMY_ENGINE_OPTIONS = SQLALCHEMY_ENGINE_OPTIONS


config = {
    "default": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestingConfig,
}
