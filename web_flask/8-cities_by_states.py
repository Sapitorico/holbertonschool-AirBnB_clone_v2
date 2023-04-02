#!/usr/bin/python3
""" Task 8 module """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays states and their cities"""

    from models.state import State
    from models import storage

    states_dict = storage.all(State)

    states_list = sorted(states_dict.values(), key=operator.attrgetter('name'))

    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def close_session(exception):
    """Closes SQLAlchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
