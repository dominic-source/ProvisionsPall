#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify
import json


@app_views.route('/store', strict_slashes=False, methods=['GET'])
def get_stores():
    """Get all the stores as requested"""
    
    # Get random stores
    with open('api/data_for_testing/store.json', 'r', encoding='utf-8') as fd3:
        stores = json.load(fd3)

    return jsonify(stores[0:20])

@app_views.route('/store_search', strict_slashes=False, methods=['POST'])
def find_store():
    """Find stores matching the parameters"""

    return jsonify({'id': 'asjfjajskfkjj', 'store': 'fadsfagea'})