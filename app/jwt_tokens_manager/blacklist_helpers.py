from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound

from app.models import TokenBlacklist
from app import db


def _epoch_utc_to_datetime(epoch_utc):
    return datetime.fromtimestamp(epoch_utc)


def add_token_to_database(decoded_token, identity_claim):
    """
    Adds a decoded token to the database.
    :param decoded_token:
    :param identity_claim:
    :return:
    """
    jti = decoded_token['jti']
    token_type = decoded_token['type']
    user_identity = decoded_token[identity_claim]
    expires = _epoch_utc_to_datetime(decoded_token['exp'])

    db_token = TokenBlacklist(
        jti=jti,
        token_type=token_type,
        user_identity=user_identity,
        expires=expires,
    )
    db.session.add(db_token)
    db.session.commit()


def is_token_revoked(decoded_token):
    """
     Checks if the given token is revoked or not. Because we are adding all the
    tokens that we create into this database, when user completes logout request, if the token is not present
    in the database we are going to consider it revoked, as we don't know where
    it was created.
    :param decoded_token:
    :return:
    """
    jti = decoded_token['jti']
    try:
        TokenBlacklist.query.filter_by(jti=jti).one()
        return True
    except NoResultFound:
        return False
