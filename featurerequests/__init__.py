import os
from flask import Flask
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_env_variable(name, default=None):
    u"""
    Get the environment variables.
    An attempt to get the variable name from the env and when not found,
    raise an error, ImprorerlyConfigured.
    """
    try:
        return os.environ[name]
    except KeyError:
        if default:
            return default
        raise ImportError(
            'Set the {0} environment variable.'.format(name)
        )


def read_env_variable():
    u"""
    Read the environment variables from .env file.

    Define the PATH for the .env file and Load the .env
    """
    dotenv_path = os.path.join(BASE_DIR, '.env')
    try:
        load_dotenv(dotenv_path)
    except IOError:
        raise
        pass


read_env_variable()

app = Flask(__name__)
env = get_env_variable(
    'SETTINGS_MODULE', 'featurerequests.settings.Config')
app.config.from_object(env)
app.config['ENV'] = env


from featurerequests import views


if __name__ == "__main__":
    app.run(debug=True)
