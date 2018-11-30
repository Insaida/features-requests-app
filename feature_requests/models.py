from feature_requests import app

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class FeaturesRequest(db.Model):
    """[summary]

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
    client = db.relationship('Client', backref='features_requests')
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    client_priority = db.Column(db.Integer, default=1)
    product_area_id = db.Column(
        db.Integer,
        db.ForeignKey('product_area.id'),
        nullable=False
    )
    target_date = db.Column(db.Date, nullable=False)
    product_area_id = db.Column(
        db.Integer,
        db.ForeignKey('product_area.id'),
        nullable=False
    )

    def __repr__(self):
        return '<FeaturesRequest %r>' % self.title

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