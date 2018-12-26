from flask_jwt_extended import get_jwt_identity, create_access_token
from app.response import json_response


def refresh_token():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user, fresh=False)

    return json_response({'access_token': new_access_token}, 201)
