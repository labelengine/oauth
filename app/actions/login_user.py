from app.response import error_message, json_response
from flask_jwt_extended import create_access_token
from app.models import User
from app import bcrypt


def login_user(username: str, password: str):
    if not username:
        return error_message("Missing username parameter")
    if not password:
        return error_message("Missing password parameter")

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return error_message("Wrong username or password", 401)

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return json_response({'access_token': access_token})
