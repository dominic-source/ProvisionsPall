#!/usr/bin/python3
"""This module handles the route for provisions pall"""
from flask import render_template, request, jsonify, make_response, redirect, url_for
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from provisionspall_web import app, db
from models.model import User, User_Address, Store, Store_Address, Product


cors = CORS(app, resources={r'/api/v1': {'origins': '*'}})

@app.route("/", strict_slashes=False)
def landing_page():
    """This is the first route for test the api"""

    return render_template('landing_page.html')

@app.route('/dashboard/<id>', strict_slashes=False)
def dashboard(id):
    """To help us render the dashboard page"""

    return render_template('dashboard.html')

@app.route('/store', strict_slashes=False)
def store():
    """To help us render the store page"""

    return render_template('store.html')

@app.route('/market', strict_slashes=False)
def market():
    """To help us render the market page"""

    return render_template('market.html')

@app.route('/login', strict_slashes=False, methods=["GET", "POST"])
def login():
    """To help us render the login page"""
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = db.session.query(User).all()
        for user in users:
            if user.username == username:
                if user.password == password:
                    return redirect(url_for("dashboard", id=user.id))
                else:
                    return jsonify({"error": "Wrong password"}), 200
        return jsonify({"error": "Not registered"}), 200
        

@app.route('/register', strict_slashes=False, methods=["GET", "POST"])
def register():
    """To help us render the login page"""
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
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

            return redirect('/dashboard/' + str(user.id))
        except IntegrityError as e:
            db.session.rollback()
           
            return jsonify({'error': 'user already registered'})
        except Exception as e: 
         
            db.session.rollback()
            return jsonify({'error': 'An unexpected error occured'})


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')