from flask_jwt_extended import create_access_token, create_refresh_token


def create_tokens(identity):
    """
    Returns access and refresh tokens and adds a new tokens to the database
    :param identity:
    :return:
    """
    access_token = create_access_token(identity=identity, fresh=True)
    refresh_token = create_refresh_token(identity=identity)

    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
