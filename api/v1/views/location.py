#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from flask import jsonify, request
from api.v1.views import app_views
from models.model import Store_Address
from api.v1 import db



@app_views.route('/locate/<store_id>', strict_slashes=False, methods=['GET'])
def locate_me(store_id):
    """Get current location of users"""

    # Check the user or stores location from the database
    # if present return information
    # else get information from google map or other 3rd party api
    # Get random locations
    if request.method == 'GET':
        try:
            data = db.session.get(Store_Address, store_id)
            address_data = { 
                                'number': data.number,
                                'street':data.street,
                                'area': data.area,
                                'city': data.city,
                                'country': data.country,
                                'longitude': data.longitude,
                                'latitude': data.latitude
                            }
            return jsonify(address_data), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'Error': 'An error occurred while trying to get store location'})
    


@app_views.route('/all_stores', strict_slashes=False, methods=['GET'])
def locate_all_stores():
    """Get all location of users stores"""
    if request.method == 'GET':
        try:
            stores = db.session.query(Store_Address).all()
            all_store_addresses = []
            if stores:
                for data in stores:
                    address_data = { 
                                        'number': data.number,
                                        'street':data.street,
                                        'area': data.area,
                                        'city': data.city,
                                        'country': data.country,
                                        'longitude': data.longitude,
                                        'latitude': data.latitude
                                    }
                    all_store_addresses.append(address_data)
                return jsonify(all_store_addresses), 200
            else:
                return jsonify({'Message': 'No Stores address for now'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'Error': 'An error occurred while trying to get store location'})
    
   
