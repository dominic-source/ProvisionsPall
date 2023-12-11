#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import jsonify, request
from api.v1 import db
from models.model import Product, Store
from provisionspall_web import UPLOAD_FOLDER, allowed_file
import os
from werkzeug.utils import secure_filename

@app_views.route('/<store_id>/product', strict_slashes=False, methods=['POST', 'GET'])
def products(store_id=None):
    """Get all the products"""
    # get all the products

    if request.method == 'POST':
        
        # Handle file uploads
        file = request.files.get('file')
        filename = ''
        if file and allowed_file(file.filename):                
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        if store_id:
            options = {
                'name': request.form.get('name'),
                'price': request.form.get('price'),
                'description': request.form.get('description'),
                'category': request.form.get('category'),
                'store_id': store_id,
                'image': filename
            }
        try:
            product = Product(**options)
            # Get the store
            store = db.session.get(Store, store_id)
            store.products.append(product)
            db.session.commit()
            return jsonify({'Message': 'Success creating product', 'product_id': product.id, 'status': 'success'}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'Error': 'Error creating a product'}), 400
    elif request.method == 'GET':
        if store_id:
            try:
                store = db.session.get(Store, store_id)
                products = store.products
                all_products = []
                for data in products:
                    options = {
                        'name': data.name,
                        'price': data.price,
                        'description': data.description,
                        'category': data.category,
                        'id': data.id,
                        'image': data.image,
                        'date_created': data.date_created,
                        'store_id': data.store_id
                    }
                    all_products.append(options)
                return jsonify(all_products), 200
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({'Error': 'An error was encountered'}), 400
   
@app_views.route('/product/<product_id>', strict_slashes=False, methods=['PUT', 'GET', 'DELETE'])
def update_product(product_id=None):
    """Update a product"""
    
    if request.method == 'PUT':
        # json_data = request.get_json()
        if product_id:
            options = {
                'name': request.form.get('name'),
                'price': request.form.get('price'),
                'description': request.form.get('description'),
                'category': request.form.get('category'),
                'image': request.form.get('image')
            }
        try:
            data = db.session.get(Product, product_id)
            for key, value in options.items():
                if value:
                    setattr(data, key, value)
            db.session.commit()
            return jsonify({'Message': 'Product updated successfully', 'product_id': data.id}), 200
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({'Error': 'An error was encountered'}), 400

    elif request.method == 'GET':
        if product_id:
            try:
                data = db.session.get(Product, product_id)
                options = {
                    'name': data.name,
                    'price': data.price,
                    'description': data.description,
                    'category': data.category,
                    'id': data.id,
                    'date_created': data.date_created,
                    'store_id': data.store_id,
                    'image': data.image,
                }
                return jsonify(options), 200
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({'Error': 'An error was encountered'}), 400
    elif request.method == 'DELETE':
        if product_id:
            try:
                data = db.session.get(Product, product_id)
                db.session.delete(data)
                db.session.commit()
                return jsonify({'Message': 'Succesfully deleted'}), 200
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({'Error': 'An error was encountered'}), 400

    
@app_views.route('/products_search', strict_slashes=False, methods=['POST'])
def products_search():
    """Get all the products"""
    # search for products
    return jsonify({'id': '4325tstr', 'name': 'mango fruits'})
