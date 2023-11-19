#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify

@app_views('/users/<id>', strict_slashes=False, methods=['GET'])
def get_users(id):
    """Get all the users of our platform"""

    return jsonify({'id': 'falsf', 'mfaslfm': 'fawa'})