#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from flask import render_template, make_response, jsonify
from api.v1.views import app_views
import json

@app_views.route('/location/<id>', strict_slashes=False)
def locate_me(id):
    """Get current location of users"""

    # Check the user or stores location from the database
    # if present return information
    # else get information from google map or other 3rd party api
    # Get random locations
    with open('api/data_for_testing/location.json', 'r', encoding='utf-8') as fd1:
        locations = json.load(fd1)
    return make_response(jsonify(locations[0: 20]), 200)
