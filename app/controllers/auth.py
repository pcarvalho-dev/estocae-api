from flask import request

from app.controllers.user import crud_user
from app.services.errors.exceptions import UnauthorizedError
from app.services.jwt.token import generate_user_jwt
from app.services.security.password import verify_password


def auth_login():
    """
    It checks if the user is an admin or not, and then checks if the user exists in the database

    :param basic: "NDRleHByZXNzYWRtaW46NDRleHByZXNzcGFzc3dvcmQ="
    :param params: {'grant_type': 'password', 'username': 'admin@admin.com', 'password': 'admin'}
    :return: A tuple with the user and the password
    """

    basic = request.headers.get("Authorization", None)
    if not basic:
        raise UnauthorizedError("Invalid Basic Negado Header")

    dict_body = request.get_json()

    if dict_body["grant_type"] != "password":
        raise UnauthorizedError("Grant Type Errado")

    user = crud_user.validate_auth_request(username=dict_body['username'],
                                           basic=basic)

    if user is not None and verify_password(user.password,
                                            dict_body['password']):
        user_token = generate_user_jwt(user)

        return user_token, 200
    else:
        raise UnauthorizedError("Usuário ou Senha incorreta!")


def auth_refresh(user_jwt):
    user = crud_user.get_user_by_jwt(user_jwt)
    if user:
        user_token = generate_user_jwt(user)
        return user_token, 200
    else:
        raise UnauthorizedError("Usuário não autorizado!")
