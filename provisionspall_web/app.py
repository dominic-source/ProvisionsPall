#!/usr/bin/python3
"""This module handles the route for provisions pall"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def first_route():
    """This is the first route for test the api"""

    return render_template('file.html')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

