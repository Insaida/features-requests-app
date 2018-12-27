from featurerequests import get_env_variable

from dotenv import load_dotenv
load_dotenv()


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_env_variable(
        'DATABASE_URL',
        default="sqlite:///:memory:"
    )
    SECRET_KEY = get_env_variable('SECRET_KEY', default='we_wchu_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True
