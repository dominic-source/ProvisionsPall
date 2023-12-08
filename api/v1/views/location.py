#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from flask import jsonify, request
from api.v1.views import app_views
from models.model import Store_Address, Store, User
from api.v1 import db


@app_views.route('/locate/<store_id>', strict_slashes=False, methods=['GET'])
def locate_me(store_id):
    """Get current location of users store"""
    # Check the user or stores location from the database
    # if present return information

    if request.method == 'GET':
        try:
            data = db.session.get(Store, store_id)
            userinfo = db.session.get(User, data.user_id)
            if data.addresses:
                addresses = []
                geoJson = { "type": "FeatureCollection",
                            "features": []}
                for addr in data.addresses:
                    address_data = { 
                                        'store_name': data.name,
                                        'number': addr.number,
                                        'street':addr.street,
                                        'area': addr.area,
                                        'city': addr.city,
                                        'country': addr.country,
                                        'longitude': addr.longitude,
                                        'latitude': addr.latitude
                                    }
                    geo_data = {
                                    "geometry": {
                                        "type": "Point",
                                        "coordinates": [addr.longitude,
                                            addr.latitude
                                        ]
                                    },
                                    "type": "Feature",
                                    "properties": {
                                        "category": "patisserie",
                                        "hours": "9am - 6pm",
                                        "description": data.description,
                                        "name": str(userinfo.last_name) + ' ' + str(userinfo.first_name),
                                        "phone": str(userinfo.email),
                                        "storeid": data.id
                                    }
                                }
                    addresses.append(address_data)
                    geoJson['features'].append(geo_data)
                return jsonify({'geoJsonFormat': geoJson, 'addressFormat': addresses}), 200

        except Exception as e:
            print(e)
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
                                        'id': data.id,
                                        'store_id': data.store_id,
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
    
   
