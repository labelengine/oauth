from app.response import error_message, json_response
from app.models import User
from app import bcrypt
from app.jwt_tokens_manager.create_tokens import create_tokens


def login_user(username: str, password: str):
    if not username:
        return error_message("Missing username parameter")
    if not password:
        return error_message("Missing password parameter")

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return error_message("Wrong username or password", 401)

    tokens = create_tokens(identity=username)

    return json_response(tokens)
