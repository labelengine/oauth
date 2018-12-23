from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
# FIXME: Move options to config
app.config['JWT_SECRET_KEY'] = 'koryun-khachatryan'  # Change this!
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_ERROR_MESSAGE_KEY'] = 'message'
jwt = JWTManager(app)

# TODO: set as env variables
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = '127.0.0.1'
DB_NAME = 'identities'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy(app)

# It is a Flask extension that provides bcrypt hashing utilities for application.
bcrypt = Bcrypt(app)

# Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
# The database operations are made available through the Flask command-line interface
migrate = Migrate(app=app, db=db)

from app import routes
from app import models
