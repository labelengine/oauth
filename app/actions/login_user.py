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
    if not user:
        return error_message("User name not found", 401)
    if not bcrypt.check_password_hash(user.password, password):
        return error_message("Wrong password", 401)

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return json_response({'access_token': access_token})
