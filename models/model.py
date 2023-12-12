#!/usr/bin/python3
"""Create models for the application
    here are the models: 
        User
        Store
        Product
        User_Address
        Store_Address
"""
from datetime import datetime
from provisionspall_web import db

class User(db.Model):
    """ Model for user basic info """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image = db.Column(db.String(150), nullable=True, default='chinonso')
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    addresses = db.relationship('User_Address', backref='user', lazy=True, cascade='all, delete-orphan')
    stores = db.relationship('Store', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        """ Representation of the User model """
        return f"User('{self.username}', '{self.email}')"


class User_Address(db.Model):
    """ Model for user address """
    id = db.Column(db.Integer, primary_key=True)
    house_no = db.Column(db.Integer)
    street = db.Column(db.String(120))
    area = db.Column(db.String(120))
    city = db.Column(db.String(120))
    country = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """ Representation of the User_Address model """
        return f"{self.user}: Address({self.house_no} {self.street}, {self.city})\n"


class Store(db.Model):
    """ Model for store basic info """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(150), nullable=True, default='img14')
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    addresses = db.relationship('Store_Address', backref='store', lazy=True, cascade='all, delete-orphan')
    products = db.relationship('Product', backref='store', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        """ Representation of the Store model """
        return f"{self.user}: Store({self.name})"


class Store_Address(db.Model):
    """ Model for store address """
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    street = db.Column(db.String(120), nullable=False)
    area = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=False)
    longitude = db.Column(db.Integer)
    latitude = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

    def __repr__(self):
        """ Representation of the Store_Address model """
        return f"{self.store}: Address({self.number} {self.street}, {self.city})\n"


class Product(db.Model):
    """Model for products in stores"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(150), nullable=True, default='img4')
    category = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)

    def __repr__(self):
        """ Representation of the Product model """
        return f"{self.store}: Product({self.name}, Category: {self.category}\n"