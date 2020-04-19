import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # JWT CONF
    JWT_SECRET_KEY = '0e9jc9nh2cemdsunac89sd0cx=-30e=c920cn0iemdweyty'
    JWT_ALGORITHM = os.environ.get('JWT_SECRET', "HS256")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=15)

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:t3sting$20@test.cm3atlknp5l3.us-east-1.rds.amazonaws.com/project"

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
    SQLALCHEMY_DATABASE_URI = "postgresql://project@psql/project"

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
