#!/usr/bin/python3
""" Task 8 module """

from os import getenv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_city_print():
    """prints state and city"""

    from models import storage
    from models.state import State

    states_dict = storage.all(State).values()
    states_city_dict = {}

    for state in states_dict:
        states_city_dict[state] = state.cities

    return render_template('8-cities_by_states.html',
                           states_city_dict=states_city_dict)


@app.teardown_appcontext
def closing(dummy):
    """closes alchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)