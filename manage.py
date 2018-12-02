#!/usr/bin/env python3

import argparse
import json
import os

from featurerequests import app, models
from flask_fixtures import load_fixtures

help_message = """"
usage: python3 manage.py [command]

where [command] can be replaced with any of these arguments:
runserver;
init_db;
create_db;
drop_db



"""

help_description = "Script for managing this application and its functions"

if __name__ == "__main__":
    app_parser = argparse.ArgumentParser(
        description=help_description,
        formatter_class=argparse.RawTextHelpFormatter
    )
    app_parser.add_argument('command', help=help_message)
    args = app_parser.parse_args()

    if args.command == "runserver":
        app.run()
    elif args.command == "create_db":
        models.db.create_all()
    elif args.command == "init_db":
        fixture_dir_path = os.path.join('featurerequests', 'fixtures')
        for fixture in os.listdir(fixture_dir_path):
            fixture_path = os.path.join(fixture_dir_path, fixture)
            with open(fixture_path, 'r') as loader:
                load_fixtures(models.db, json.loads(loader.read()))
    elif args.command == "drop_db":
        models.db.drop_all()
