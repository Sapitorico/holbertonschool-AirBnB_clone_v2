#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
"""text variable to be displayed on the route"""


""" application of Flask variable"""
app = Flask(__name__)
"""text variable to be displayed on the route"""


@app.route('/', strict_slashes=False)
def index1():
    """text variable to be displayed on the route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def index():
    """text variable to be displayed on the route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def index(text):
    """text variable to be displayed on the route"""
    return f"C {text}"


if __name__ == '__main__':
    """ starts a Flask web application """
    app.run(debug=True, host='0.0.0.0', port=5000)
