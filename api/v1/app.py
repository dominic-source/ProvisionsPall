#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

cors = CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})

@app.teardown_appcontext
def close_db(error):
    """Close the database"""
    pass

@app.errorhandler(404)
def not_found(error):
    """Returns 404 error with and object indicate not found"""

    return make_response(jsonify({'error': 'not found'}), 404)

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5001)
    