from flask import jsonify
from flask_jwt_extended import JWTManager

jwt = JWTManager()


@jwt.invalid_token_loader
def expired_token_callbacks(c):
    """
    It returns a JSON response with a status code of 422 and a message of "Token não processado" when
    the token is expired
    
    :param c: The context of the request
    :return: A tuple with two elements:
    1. A jsonified dictionary
    2. A status code
    """
    return jsonify({
        'status': 422,
        'msg': f'Token não processado'
    }), 422


@jwt.unauthorized_loader
def expired_token_callback(c):
    """
    If the token is expired, return a 401 error
    
    :param c: The current application context
    :return: A tuple with two elements:
    1. A response object
    2. A status code
    """
    return jsonify({
        'status': 401,
        'msg': f'Token não enviado'
    }), 401
