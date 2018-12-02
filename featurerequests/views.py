from flask import jsonify, render_template, request

from featurerequests import app

from featurerequests.models import db, FeaturesRequest, Client, ProductArea


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/api/feature_requests/", methods=("GET"))
def feature_requests_get_method():
    feature_requests = FeaturesRequest.query.all()
    