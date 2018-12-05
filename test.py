import os
import json
import unittest
import tempfile

from datetime import datetime

from featurerequests import app
from featurerequests.models import db, User, FeaturesRequest, Client, ProductArea


app.config.from_object('featurerequests.settings.TestingConfiguration')


class FeatureRequestTestCase(unittest.TestCase):
    fixtures = ['clients.json', 'product_areas.json', 'users.json']
    app, db = app, db
    post_data = {
        "user": 1,
        "client": 1,
        "product_area": 1,
        "title": "First Feature Request",
        "client_priority": 1,
        "description": "First Feature Request description",
        "target_date": str(datetime.utcnow().date())
    }

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        db.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    
if __name__ == '__main__':
    unittest.main()
