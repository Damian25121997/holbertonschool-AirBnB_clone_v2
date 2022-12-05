#!/usr/bin/python3
"""
Script that starts a web application
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    from models import storage
    """ close files storage
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    from models import storage
    from models.state import State
    """ display states in html page
    """
    context = storage.all(State)
    return render_template('9-states.html', states=context)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    from models import storage
    from models.state import State
    """ display state in html page
    """
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
