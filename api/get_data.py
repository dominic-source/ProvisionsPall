#!/usr/bin/python3
import requests
import json
import uuid

def create_data():
    """Create temporary data for our database and for testing purposes"""
    resp = requests.get('https://randomuser.me/api/?page=1&results=100&seed=abc')

    if resp.status_code != requests.codes.ok:
        print("No response")
        return None
    data = resp.json().get('results')  # Parse the JSON response
    
    user = []
    store = []
    location = []
    product = []

    for data_entry in data:
        # create a user dictionary    
        info = {
            'gender': data_entry.get('gender'),
            'email': data_entry.get('email'),
            'login': data_entry.get('login'),
            'dob': data_entry.get('dob'),
            'registered': data_entry.get('registered'),
            'phone': data_entry.get('phone'),
            'id': data_entry.get('login').get('uuid')
        }
        info.update(data_entry.get('name'))
        user.append(info)

        # create a store dictionary
        info_store = {
            'id': data_entry.get('login').get('uuid'),
            'user_id': info['id'],
            'name': data_entry.get('location').get('city'),
            'description': data_entry.get('location').get('timezone').get('description')
        }
        store.append(info_store)

        # create a location dictionary
        info_location = data_entry.get('location')
        location.append(info_location)

        # create a product dictionary
        info_product = {
            'id': str(uuid.uuid4()),
            'user_id': info['id'],
            'store_id': info_store['id'],
            'name': data_entry.get('id').get('name'),
            'Description': info_store['description'],
            'Category': data_entry.get('nat')
        }
        product.append(info_product)

    with open('user.json', 'w', encoding='utf-8') as fd:
        json.dump(user, fd)
    with open('store.json', 'w', encoding='utf-8') as fd2:
         json.dump(store, fd2)
    with open('location.json', 'w', encoding='utf-8') as fd3:
         json.dump(location, fd3)
    with open('product.json', 'w', encoding='utf-8') as fd4:
        json.dump(product, fd4)

if __name__ == '__main__':
    create_data()
