#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import request, jsonify
from models.model import User
from api.v1 import db


@app_views.route('/user/<id>', strict_slashes=False, methods=['DELETE'])
def delete_user(id=None):
    """This will delete a single user"""
    
    if request.method == 'DELETE' and id is not None:
        try:
            user_del = db.session.get(User, id)
            db.session.delete(user_del)
            db.session.commit()
            return jsonify({'Message': 'successfully deleted the user'})
        except Exception:
            db.session.rollback()
            return jsonify({'Error': 'Could not delete the user'}), 400
    else:
        return jsonify({'Error': 'Id is required or requirement was not met'}), 400      


@app_views.route('/user', strict_slashes=False, methods=['POST'])
@app_views.route('/user/<id>', strict_slashes=False, methods=['PUT'])
def create_or_update_user(id=None):
    """This function will help us to create or update a user information"""
    if request.method == 'POST':
        options = {
            'username': request.form.get('username'),
            'first_name': request.form.get('firstname'),
            'last_name': request.form.get('lastname'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }
        try:
            user = User(**options)
            db.session.add(user)
            db.session.commit()
            return jsonify({'Message': 'User create successfully', 'user_id': user.id}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'Error': 'Unable to create User'}), 404
    if request.method == 'PUT':
        if id is None:
            return jsonify({'Requirement': 'User id is required'}), 404
        else:
            options = {
            'username': request.form.get('username'),
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
            }
            try:
                data = db.session.get(User, id)
                for key, value in options.items():
                    if value is not None:
                        setattr(data, key, value)
                db.session.commit()
                return jsonify({'Message': 'User updated successfully', 'user_id': data.id}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'Error': 'An error was encountered'}), 400
       
@app_views.route('/users', strict_slashes=False, methods=['GET'])
@app_views.route('/user/<id>', strict_slashes=False, methods=['GET'])
def get_users(id=None):
    """Get all the users of our platform"""
    if request.method == 'GET':
        # returns all the users, their stores and their addresses
        try:
            if id is None:
                objects = db.session.query(User).all()
            else:
                d_object = db.session.get(User, id)
                objects = [d_object,]
            all_data = []
            for object_d in objects:
                product_count = 0
                data = {
                    'id': object_d.id,
                    'username': object_d.username,
                    'first_name': object_d.first_name,
                    'last_name': object_d.last_name,
                    'email': object_d.email,
                    'date_registered': object_d.date_created,
                    'addresses': [],
                    'stores': [],
                    'products': product_count,
                }
                if object_d.addresses:
                    for addr in object_d.addresses:
                        addr_s = {
                            'id': addr.id,
                            'house_no': addr.house_no,
                            'street': addr.street,
                            'area': addr.area,
                            'city': addr.city,
                            'country': addr.country,
                        }
                        data['addresses'].append(addr_s)
                if object_d.stores:
                    for store in object_d.stores:
                        store_s = {
                            'id': store.id,
                            'name': store.name,
                            'description': store.description,
                            'data_created': store.date_created,
                            'products': len(store.products),
                        }
                        data['stores'].append(store_s)
                        data['products'] += len(store.products)
                all_data.append(data)
            return jsonify(all_data), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'Error': 'An error was encountered'}), 404
       