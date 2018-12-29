from app import db


class User(db.Model):
    __tablename__ = 'users'

    # FIXME: id field must be uuid type
    id = db.Column(db.Integer, primary_key=True)
    # The collation = 'NOCASE' is required to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='NOCASE'), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')


class Role(db.Model):
    __tablename__ = 'roles'

    # FIXME: id field must be uuid type
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'

    # FIXME: id field must be uuid type
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class TokenBlacklist(db.Model):
    __tablename__ = 'token_blacklist'

    # FIXME: id field must be uuid type
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    token_type = db.Column(db.String(10), nullable=False)
    user_identity = db.Column(db.String(50), nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
