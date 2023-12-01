#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify
import json
from models.model import User, User_Address, Store, Store_Address, Product
from api.v1 import db


@app_views.route('/', strict_slashes=False, methods=['GET'])
@app_views.route('/users', strict_slashes=False, methods=['GET'])
def get_users():
    """Get all the users of our platform"""
    # Get random users
    with open('api/data_for_testing/user.json', 'r', encoding='utf-8') as fd4:
        users = json.load(fd4)
    info = []
    for data in users:
        info.append(data['id'])

    return make_response(jsonify(info[0:100]), 200)

@app_views.route('/users/<id>', strict_slashes=False, methods=['GET'])
def get_user_one(id):
    """Get all the users of our platform"""

    # Get random users
    with open('api/data_for_testing/user.json', 'r', encoding='utf-8') as fd4:
        users = json.load(fd4)

    for data in users:
        if id == data['id']:
            return jsonify(data)
    return jsonify({'Error': 'not found'}), 404