#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask


""" application of Flask variable"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index1():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index2():
    return "HBNB"


if __name__ == '__main__':
    """ starts a Flask web application """
    app.run(debug=True, host='0.0.0.0', port=5000)
