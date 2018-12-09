from featurerequests import app
from featurerequests.settings import ProductionConfiguration

app.config.from_object(ProductionConfiguration)

import featurerequests.views
