from flask import Flask
from flask_jwt_extended import JWTManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
moment = Moment()
jwt_manager = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config['default'].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    jwt_manager.init_app(app)
    from .api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    return app
