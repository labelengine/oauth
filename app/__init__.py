from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config.from_object('app.config.BaseConfig')
jwt = JWTManager(app)
db = SQLAlchemy(app)
# It is a Flask extension that provides bcrypt hashing utilities for application.
bcrypt = Bcrypt(app)
# Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
# The database operations are made available through the Flask command-line interface
migrate = Migrate(app=app, db=db)

from app import routes
from app import models
