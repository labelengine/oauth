from app import app, jwt
from flask import request
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from app.actions.register_user import register_user
from app.actions.login_user import login_user
from app.actions.logout_user import logout_user
from app.jwt_tokens_manager.refresh_token import refresh_token
from app.jwt_tokens_manager.blacklist_helpers import is_token_revoked


# FIXME: move method from routes.py
@jwt.token_in_blacklist_loader
def check_if_token_revoked(decoded_token):
    return is_token_revoked(decoded_token)


@app.route('/registration', methods=['POST'])
def registration():
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    return register_user(username, email, password)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    return login_user(username, password)


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    return refresh_token()


@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    return logout_user()
