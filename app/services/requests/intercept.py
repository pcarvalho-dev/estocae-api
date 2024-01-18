from functools import wraps

from flask_jwt_extended import get_jwt_identity

from app.services.errors.exceptions import UnauthorizedError


def intercept_admin_user(f):
    """
    If the user is not an admin, raise an error
    
    :param f: The function to be decorated
    :return: The function is being returned.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        jwt_group_id = get_jwt_identity()['group_id']

        if jwt_group_id == 5:
            raise UnauthorizedError('Usuário não autorizado!')

        return f(*args, **kwargs)

    return wrap
