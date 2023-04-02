#!/usr/bin/python3
""" create a script that starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def close_session(response_or_exc):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=500)