from app import app
from flask import request
from app.actions.register_user import register_user
from app.actions.login_user import login_user


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
