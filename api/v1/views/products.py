#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify

@app_views('/products', strict_slashes=False, methods=['GET'])
def products():
    """Get all the products"""
    # get all the products
    return jsonify({'id': '4325tstr', 'name': 'mango fruits'})


@app_views('/products_search', strict_slashes=False, methods=['POST'])
def products_search():
    """Get all the products"""
    # search for products
    return jsonify({'id': '4325tstr', 'name': 'mango fruits'})
