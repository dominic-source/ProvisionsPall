from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# To Include migration for our database updates
from flask_migrate import Migrate
import os
import secrets


# Start the flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configure the file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Determines the absolute path for the upload folder
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# To generate secret keys for managing sessions cookies
app.secret_key = secrets.token_hex()

# Add google map api key to configuration
app.config['API_KEY'] = 'AIzaSyCtRXnkNE4h6eeqCg0IoTyMXqyHrfbOYLI'

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
