from app.response import error_message, json_response
from flask_jwt_extended import create_access_token
from app.models import User


def login_user(username: str, password):
    if not username:
        return error_message("Missing username parameter")
    if not password:
        return error_message("Missing password parameter")

    if not User.query.filter_by(username=username).first():
        return error_message("User name not found", 404)

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return json_response({'access_token': access_token})
