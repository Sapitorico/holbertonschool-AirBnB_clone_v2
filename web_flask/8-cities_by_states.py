#!/usr/bin/python3
""" Task 8 module """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays states and their cities"""

    states_dict = storage.all(State)

    states_city_dict = {}
    for state in states_dict.values():
        states_city_dict[state] = sorted(state.cities, key=lambda c: c.name)

    states_list = sorted(states_dict.values(), key=lambda s: s.name)

    return render_template('8-cities_by_states.html',
                           states_list=states_list,
                           states_city_dict=states_city_dict)


@app.teardown_appcontext
def close_session(exception):
    """Closes SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)