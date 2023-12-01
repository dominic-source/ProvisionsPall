#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify, request
from models.model import User, User_Address, Store, Store_Address, Product
from api.v1 import app, db


@app_views.route('/user/<user_id>/store/<store_id>', strict_slashes=False, methods=['DELETE'])
def delete_store(store_id):
    """Delete a store using the store id"""
    
    if request.method == 'DELETE':
        try:
            store_del = db.session.get(Store, store_id)
            db.session.delete(store_del)
            db.session.commit()
            return jsonify({'Message': 'successfully deleted the store'})
        except Exception:
            db.session.rollback()
            return jsonify({'Error': 'Could not delete the store'})


@app_views.route('/user/<user_id>/store', strict_slashes=False, methods=['GET', 'POST', 'PUT'])
def get_stores(user_id):
    """Get all the stores as requested"""
    
    if request.method == 'GET':
        # Get all store of a User
        try:
            user_stores = db.session.query(User).filter(User.id == user_id).one().stores
            all_stores = []
            for store in user_stores:
                store_details = {
                    'id': store.id,
                    'name': store.name,
                    'description': store.description,
                    'date_created': store.date_created,
                    'user_id': store.user_id
                }
                all_stores.append(store_details)
            return jsonify(all_stores)

        except Exception: 
            db.session.rollback()
            return jsonify({'Error': 'Could not get store data at this time'})
    elif request.method == 'POST' or request.method == 'PUT':
        try:
            options = {
                'name': request.form.get('name'),
                'description': request.form.get('description'),
            }
            address_options = { 
                                'number': request.form.get('number'),
                                'street':request.form.get('street'),
                                'area': request.form.get('area'),
                                'city': request.form.get('city'),
                                'country': request.form.get('country'),
                                'longitude': request.form.get('longitude'),
                                'latitude': request.form.get('latitude')
                                }
            if request.method == 'POST':
                address = Store_Address(**address_options)
                store = Store(**options)
                store.user_id = user_id
                address.store_id = store.id
                store.addresses = [address]
                db.session.add(store)
                db.session.commit()
                return jsonify({'message': 'Store created successfully'})
            else:
                store_id = request.form.get('store_id')
                store_address_id = request.form.get('store_address_id')
                update_store = db.session.get(Store, store_id)
                update_store_address = db.session.get(Store_Address, store_address_id)
                if update_store and update_store_address:
                    for key, value in options:
                        setattr(update_store, key, value)
                    for key, value in address_options:
                        setattr(update_store_address, key, value)
                    db.session.commit()
                else:
                    return jsonify({'Message': 'Not found'})
                
        except Exception:
            db.session.rollback()
            return jsonify({'Error': 'Error create Store'})

      
@app_views.route('/store', strict_slashes=False, methods=['GET'])
def all_stores():
    """Find stores matching the parameters"""
    if request.method == 'GET':
        try:
            stores = db.session.query(Store)
            all_stores = []
            for store in stores:
                store_details = {
                    'id': store.id,
                    'name': store.name,
                    'description': store.description,
                    'date_created': store.date_created,
                    'user_id': store.user_id
                }
                all_stores.append(store_details)
            return jsonify(all_stores)

        except Exception: 
            db.session.rollback()
            return jsonify({'Error': 'Could not get all store data at this time'})
 