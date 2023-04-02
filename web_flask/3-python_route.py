#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask


""" application of Flask variable"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index1():
    """
    document
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index2():
    """
    document
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index3(text):
    """
    text variable to be displayed on the route
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/',
           defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index4(text):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
