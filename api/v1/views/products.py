#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify
import json

@app_views.route('/products', strict_slashes=False, methods=['GET'])
def products():
    """Get all the products"""
    # get all the products

    # Get random products
    with open('api/data_for_testing/product.json', 'r', encoding='utf-8') as fd2:
        products = json.load(fd2)

    return jsonify(products[0:20])


@app_views.route('/products_search', strict_slashes=False, methods=['POST'])
def products_search():
    """Get all the products"""
    # search for products
    return jsonify({'id': '4325tstr', 'name': 'mango fruits'})
