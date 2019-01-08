from app.jwt_tokens_manager.blacklist_helpers import add_token_to_database
from app import app
from app.response import json_response


def logout_user(decoded_token):
    add_token_to_database(decoded_token, app.config['JWT_IDENTITY_CLAIM'])
    return json_response({'message': "Successfully logged out"})
