#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from flask import render_template, make_response, jsonify
from api.v1.views import app_views

@app_views('/location/<id>', strict_slashes=False)
def locate_me(id):
    """Get current location of users"""

    # Check the user or stores location from the database
    # if present return information
    # else get information from google map or other 3rd party api

    return make_response(jsonify({
                                    'id': 'my id',
                                    'latitude': '0900',
                                    'longitude': '2242'
                                }), 200)
