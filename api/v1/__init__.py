from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Start the flask app
app = Flask(__name__)

# configure sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)