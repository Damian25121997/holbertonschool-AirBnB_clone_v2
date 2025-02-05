#!/usr/bin/python3
"""
Script that starts a web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def context(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_r():
    states = storage.all(State)
    all_states = []

    for state in states.values():
        all_states.append([state.id, state.name])
    return render_template('7-states_list.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
