from flask import jsonify, render_template, request

from featurerequests import app


@app.route("/")
def homepage():
    return render_template('base.html')
