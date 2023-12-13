from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
import os
# To Include migration for our database updates
from flask_migrate import Migrate

# Start the flask app
app = Flask(__name__)

# configure sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
 
# Here is the code for apply migration of models (please read the comment carefully)
# flask db init  # Initialize migrations (run this command only once)
# flask db migrate -m "Added image column to store table"
# flask db upgrade
