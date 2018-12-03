from flask import jsonify, render_template, request

from featurerequests import app

from featurerequests.models import db, FeaturesRequest, Client, ProductArea

from .schema import FeaturesRequestSchema, ClientsSchema, ProductAreaSchema

@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/api/feature_requests/", methods=["GET"])
def feature_requests_get_method():
    feature_requests = FeaturesRequest.query.all()
    feature_requests_schema = FeaturesRequestSchema()
    result = feature_requests_schema.dump(feature_requests, many=True)
    return jsonify({'feature_requests': result.data})

@app.route("/api/clients", methods=["GET"])
def clients_get_method():
    """Return list of all clients."""
    clients = Client.query.all()
    clients_schema = ClientsSchema()
    result = clients_schema.dump(clients, many=True)
    return jsonify({'clients': result.data})

@app.route("/api/product_areas/", methods=["GET"])
def product_areas_get_method():
    product_areas = ProductArea.query.all()
    product_areas_schema = ProductAreaSchema()
    result = product_areas_schema.dump(product_areas, many=True)
    return jsonify({'product_areas': result.data})

    