from flask_jwt_extended import create_access_token, create_refresh_token

from config import Config


def generate_user_jwt(user):
    """
    It creates a JWT token with the user's information and returns it
    
    :param user: the user object
    :return: A dictionary with the following keys:
    """
    try:
        user_jwt = {
            "user_id": user.id,
            "hash_id": user.hash_id,
            "name": user.name,
            "group_id": user.group_id
        }
    except:
        user_jwt = {
            "user_id": user['id'],
            "hash_id": user['hash_id'],
            "name": user['name'],
            "group_id": user['group_id']
        }

    access_token = create_access_token(identity=user_jwt)
    refresh_token = create_refresh_token(identity=user_jwt)
    data = {
        "token_type": "Bearer",
        "expires_in": Config.JWT_EXPIRES,
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return data
