#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify

@app_views('/store', strict_slashes=False, methods=['GET'])
def get_stores():
    """Get all the stores as requested"""

    return jsonify({'id': 'fsafwaf', 'name': 'Linus Chinonso Dominic Morba'})

@app_views('/store_search', strict_slashes=False, methods=['POST'])
def find_store():
    """Find stores matching the parameters"""

    return jsonify({'id': 'asjfjajskfkjj', 'store': 'fadsfagea'})