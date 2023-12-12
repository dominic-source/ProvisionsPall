#!/usr/bin/python3
"""This module handles the route for provisions pall"""
from flask import render_template, request, jsonify, make_response, redirect, url_for, session, flash
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from provisionspall_web import app, db
from models.model import User, Store, Product
import uuid

cors = CORS(app, resources={r'/api/*': {'origins': 'http://127.0.0.2:5001'}})

@app.route("/", strict_slashes=False)
def landing_page():
    """This is the first route for test the api"""

    return render_template('landing_page.html', cache_id=uuid.uuid4())

@app.route('/dashboard', strict_slashes=False)
def dashboard():
    """To help us render the dashboard page"""
    try:
        user_id = session.get('user_id')
        if user_id:
            user = db.session.get(User, user_id)
            # Add user information to dashboard
            user_info = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'id': user.id,
                'image': user.image,
                'company_name': str(user.username) + '\'s ' + 'company limited'
            }
            
            stores = user.stores
            
            store_ids = ''
            total_stores = 0
            total_products = 0
            # Add store information to dashboard
            for store in stores:
                products = db.session.query(Product)
                count_products = len(products.filter(Product.store_id == store.id).all())
                
                store_ids += str(store.id) + ' '
                total_stores += 1
                total_products += count_products


            return render_template('dashboard.html', 
                                   userdata=user_info, 
                                   storedata=store_ids,
                                   stores=total_stores,
                                   products=total_products,
                                   cache_id=uuid.uuid4()
                                   )
        else:
            return redirect('/login')
    except Exception as e:
        print(e)
        return redirect('/login')
    

@app.route('/store/<id>', strict_slashes=False)
def store(id):
    """To help us render the store page"""
    if id is None:
        return redirect('/market')
    return render_template('store.html', cache_id=uuid.uuid4(), store_id=id)

@app.route('/market', strict_slashes=False)
def market():
    """To help us render the market page"""
    store = db.session.query(Store).all()

    user_id = session.get('user_id')
    if user_id:
        logged = True
    else:
        logged = False
    return render_template('marketplace.html', 
                           stores=store, 
                           cache_id=uuid.uuid4(), 
                           logged=logged)

@app.route('/market/store/<id>', strict_slashes=False)
def market_store(id=None):
    """To help us render the market page"""
    
    if id is None:
        return redirect('/market')
    store = db.session.get(Store, id)

    if not len(store.products):
        return redirect('/market')
    return render_template('market.html', 
                           products=store.products, 
                           cache_id=uuid.uuid4())

@app.route('/logout', strict_slashes=False, methods=["GET"])
def logout(id=None):
    """To log users out of the session"""

    session.pop('user_id', None)
    return redirect("/market")  



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
                    response = make_response(redirect(url_for("dashboard", user_id=user.id)))
                    session['user_id'] = user.id
                    return response
                else:
                    return jsonify({"error": "Wrong password or username"}), 400

        return render_template("register.html", cache_id=uuid.uuid4()), 200
                

@app.route('/register', strict_slashes=False, methods=["GET", "POST"])
def register():
    """To help us render the login page"""
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        options = {
        'username': request.form.get('username'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
        }
        try:
            user = User(**options)
            db.session.add(user)
            db.session.commit()

            return redirect('/login')
        except IntegrityError as e:
            print(e)
            db.session.rollback()
           
            return jsonify({'error': 'user already registered'})
        except Exception as e: 
         
            db.session.rollback()
            return jsonify({'error': 'An unexpected error occured'})


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')