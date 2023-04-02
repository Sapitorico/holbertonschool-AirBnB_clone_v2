#!/usr/bin/python3
""" create a script that starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states.html', states=states)

@app.teardown_appcontext
def close_session(response_or_exc):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=500)