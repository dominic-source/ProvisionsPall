#!/usr/bin/python3
"""This module manages all the products of provisionspall"""

from api.v1.views import app_views
from flask import make_response, jsonify, request, abort
from models.model import Product, Store
from api.v1 import db

@app_views.route('/products', strict_slashes=False, methods=['GET'])
def get_products():
    """Get all products"""
    products = db.session.query(Product).all()
    products_list = []
    for product in products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'date_created': product.date_created,
            'store_id': product.store_id,
        })
    return jsonify(products_list)

@app_views.route('/products/<int:product_id>', strict_slashes=False, methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID"""
    product = db.session.query(Product).get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'date_created': product.date_created,
            'store_id': product.store_id,
        })
    else:
        return jsonify({'error': 'Product not found'}), 404

@app_views.route('/products', strict_slashes=False, methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.json
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        category=data['category'],
        store_id=data['store_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@app_views.route('/products/<int:product_id>', strict_slashes=False, methods=['PUT'])
def update_product(product_id):
    """Update a product by ID"""
    product = db.session.query(Product).get(product_id)
    if product:
        data = request.json
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.category = data['category']
        product.store_id = data['store_id']
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404


@app_views.route('/products/<int:product_id>', strict_slashes=False, methods=['DELETE'])
def delete_product(product_id):
    """Delete a product by ID"""
    product = Product.query.get(product_id)

    if not product:
        abort(404, description=f"Product with ID {product_id} not found")

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": f"Product with ID {product_id} has been deleted"})
