from flask_jwt_extended import get_jwt_identity, create_access_token

from app import app
from app.response import json_response
from app.jwt_tokens_manager.blacklist_helpers import add_token_to_database


def refresh_token():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user, fresh=False)
    add_token_to_database(new_access_token, app.config['JWT_IDENTITY_CLAIM'])

    return json_response({'access_token': new_access_token}, 201)
