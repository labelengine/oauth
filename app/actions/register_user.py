from app.response import error_message, json_response
from flask_jwt_extended import create_access_token
from app.models import User
from app import db, bcrypt


def register_user(username: str, email: str, password):
    if not username:
        return error_message("Missing username parameter")
    if not email:
        return error_message("Missing email parameter")
    if not password:
        return error_message("Missing password parameter")

    if User.query.filter_by(username=username).first():
        return error_message("User name already exist", 409)

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    # TODO: verify email
    # TODO: check the uniqueness of the email
    new_user = User(username=username, email=email, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return json_response({'access_token': access_token}, 201)
