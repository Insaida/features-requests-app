from .feature_requests import get_env_variable

class BaseConfiguration(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_env_variable(
        'DATABASE_URL',
        default="sqlite:///:memory:"
    )
    SECRET_KEY = get_env_variable('SECRET_KEY', default='some_secret_key')


class ProductionConfiguration(BaseConfiguration):
    DEBUG = False


class DevelopmentConfiguration(BaseConfiguration):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfiguration(DevelopmentConfiguration):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
