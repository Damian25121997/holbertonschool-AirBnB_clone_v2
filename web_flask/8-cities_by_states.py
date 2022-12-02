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


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_state', strict_slashes=False)
def cities_states():
    obj_s = storage.all('State')
    obj_c = storage.all('City')
    states = []
    cities = []
    for value in obj_s.values():
        states.append(value)
    for value in obj_c.values():
        cities.append(value)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
