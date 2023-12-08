#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models.model import User, Store, Store_Address
from api.v1 import db


@app_views.route('/user/store/<store_id>', strict_slashes=False, methods=['DELETE', 'OPTIONS'])
def delete_store(store_id):
    """Delete a store using the store id"""
    
    if request.method == 'DELETE':
        try:
            store_del = db.session.get(Store, store_id)
            db.session.delete(store_del)
            db.session.commit()
            return jsonify({'Message': 'successfully deleted the store'}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'Error': 'Could not delete the store'}), 400
    elif request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5000")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "DELETE")
        return response


@app_views.route('/user/<user_id>/stores', strict_slashes=False, methods=['GET', 'POST', 'PUT', 'OPTIONS'])
def get_stores(user_id):
    """Get all the stores as requested"""
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5000")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,OPTIONS")
        return response
    elif request.method == 'GET':
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
            return jsonify(all_stores), 200

        except Exception: 
            db.session.rollback()
            return jsonify({'Error': 'Could not get store data at this time'}), 400
    elif request.method == 'POST' or request.method == 'PUT':
        try:
            json_data = request.get_json()
            options = {
                'name': json_data['name'],
                'description': json_data['description'],
            }
            if request.method == 'POST':
                address_options = { 
                                'number': json_data['number'],
                                'street':json_data['street'],
                                'area': json_data['area'],
                                'city': json_data['city'],
                                'country': json_data['country'],
                                'longitude': json_data['longitude'],
                                'latitude': json_data['latitude']
                                }
                address = Store_Address(**address_options)
                store = Store(**options)
                store.user_id = user_id
                address.store_id = store.id
                store.addresses = [address]
                db.session.add(store)
                db.session.commit()
                return jsonify({'message': 'Store created successfully', 'store_id': store.id, 'store_address_id': address.id}), 200
            elif request.method == 'PUT':
                store_id = json_data['store_id']
                # store_address_id = request.form.get('store_address_id')
                update_store = db.session.get(Store, store_id)
                # update_store_address = db.session.get(Store_Address, store_address_id)
                if update_store:
                    for key, value in options.items():
                        if value:
                            setattr(update_store, key, value)
                    # for key, value in address_options.items():
                    #     if value:
                    #         setattr(update_store_address, key, value)
                    db.session.commit()
                    return jsonify({'Message': 'Updated successfully', 'store_id': store_id}), 200
                else:
                    return jsonify({'Message': 'Not found'}), 404
                
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'Error': 'Error create Store'}), 400

      
@app_views.route('/stores', strict_slashes=False, methods=['GET'])
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
            return jsonify(all_stores), 200

        except Exception: 
            db.session.rollback()
            return jsonify({'Error': 'Could not get all store data at this time'}), 404
 