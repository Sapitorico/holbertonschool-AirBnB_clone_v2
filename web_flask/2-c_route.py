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


@app.route('/c/<text>', strict_slashes=False)
def index3(text):
    """text variable to be displayed on the route"""
    return f"C {text}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    """ starts a Flask web application """
