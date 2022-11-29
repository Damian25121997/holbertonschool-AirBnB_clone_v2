#!/usr/bin/python3
""" A script that starts Flask web application

    Return:
        Hello HBNB!
        HBNB
        C is cool
        Python is cool
        <int>
"""


from flask import Flask
from flask import escape
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_cool(text):
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_an_int(n):
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
