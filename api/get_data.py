#!/usr/bin/python3

"""This module helps us to get random data for our application to use
    once the data has been got, there is no need to run the program again.
    
    4 files are created:
    
    location.json
    product.json
    store.json
    user.json
"""

import requests
import json
import uuid

def create_data(length=1, example=True):
    """Create temporary data for our database and for testing purposes"""
    resp = requests.get(f'https://randomuser.me/api/?results={length}')

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
    
    # to add examples instead
    if example:
        ex = '.example'
    else:
        ex = ''

    filename = 'data_for_testing/{}{}.json'
    with open(filename.format('user', ex), 'w', encoding='utf-8') as fd:
        json.dump(user, fd)
    with open(filename.format('store', ex), 'w', encoding='utf-8') as fd2:
         json.dump(store, fd2)
    with open(filename.format('location', ex), 'w', encoding='utf-8') as fd3:
         json.dump(location, fd3)
    with open(filename.format('product', ex), 'w', encoding='utf-8') as fd4:
        json.dump(product, fd4)

if __name__ == '__main__':
    create_data(length=1000, example=False)
