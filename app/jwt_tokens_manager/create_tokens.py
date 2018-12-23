from flask_jwt_extended import create_access_token, create_refresh_token
from app.jwt_tokens_manager.blacklist_helpers import add_token_to_database
from app import app


def create_tokens(identity):
    """
    Returns access and refresh tokens and adds a new tokens to the database
    :param identity:
    :return:
    """
    access_token = create_access_token(identity=identity, fresh=True)
    refresh_token = create_refresh_token(identity=identity)

    add_token_to_database(access_token, app.config['JWT_IDENTITY_CLAIM'])
    add_token_to_database(refresh_token, app.config['JWT_IDENTITY_CLAIM'])

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
