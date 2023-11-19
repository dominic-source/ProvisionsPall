#!/usr/bin/python3
"""This module handles the route for provisions pall"""
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r'/api/v1': {'origins': '*'}})

@app.teardown_appcontext
def close_dbs(error):
    """Close the database"""
    pass

@app.route("/", strict_slashes=False)
def landing_page():
    """This is the first route for test the api"""

    return render_template('landing_page.html')

@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """To help us render the dashboard page"""

    return render_template('dashboard.html')

@app.route('/store', strict_slashses=False)
def store():
    """To help us render the store page"""

    return render_template('store.html')

@app.route('/market', strict_slashes=False)
def market():
    """To help us render the market page"""

    return render_template('market.html')

@app.route('/login', strict_slashes=False)
def login():
    """To help us render the login page"""

    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
