from datetime import datetime
from featurerequests import app

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    """
    Model for IWS User who adds the features or makes the request
    """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60))

    def __repr__(self):
        return '<User %r>' % self.first_name

    __str__ = __repr__


class Client(db.Model):
    """[summary]

    Arguments:
        db {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Client %r>' % self.name

    __str__ = __repr__


class ProductArea(db.Model):
    """[summary]

Returns:
    [type] -- [description]
"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Product Area %r>' % self.name

    __str__ = __repr__


class FeaturesRequest(db.Model):
    """[Features Request Model. Contains alll the columns for this model, eg:
    Title,
    product area,
    ]

Returns:
    [type] -- [description]
"""
    id = db.Column(db.Integer, primary_key=True)
    features_title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client_id = db.Column(
        db.Integer,
        db.ForeignKey('client.id'),
        nullable=False
    )
    client = db.relationship('Client', backref='feature_requests')
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    user = db.relationship('User', backref='feature_requests')
    client_priority = db.Column(db.Integer, default=1)
    product_area_id = db.Column(
        db.Integer,
        db.ForeignKey('product_area.id'),
        nullable=False
    )
    product_area = db.relationship('ProductArea', backref='feature_requests')
    target_date = db.Column(db.Date, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow())

    def __repr__(self):
        return '<FeaturesRequest %r>' % self.title

    __str__ = __repr__
