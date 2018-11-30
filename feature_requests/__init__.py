import os
from os.path import dirname, join
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




env_file_path = join(dirname(__file__), '.env')
load_dotenv(env_file_path)


app = Flask(__name__)


app.run(debug=True)
