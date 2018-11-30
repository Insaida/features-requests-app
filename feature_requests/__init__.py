from flask import Flask
import os


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







app = Flask(__name__)





if __name__ == "__main__":
    app.run(debug=True)