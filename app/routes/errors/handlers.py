from http import HTTPStatus

import sqlalchemy
import werkzeug
from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, MethodNotAllowed

from app.services.errors.exceptions import logger, UnauthorizedError, \
    ForbiddenError, GenerateError, NotFoundError

errors_bp = Blueprint('exception_handler_bp', __name__)


@errors_bp.app_errorhandler(NotFound)
def not_found_exception(e):
    """
    It takes an exception as an argument, logs it, creates a response object with a status code of 404
    and a message, and then returns the response object
    
    :param e: The exception that was raised
    :return: A response object.
    """
    logger.exception(e)
    response = jsonify({
        "status": HTTPStatus.NOT_FOUND,
        "msg": "Recurso não encontrado"
    })
    response.status_code = HTTPStatus.NOT_FOUND
    return response


@errors_bp.app_errorhandler(UnauthorizedError)
def unauthorized_exception(e):
    """
    It takes an exception as an argument, logs the exception, creates a response object with the status
    code and error message from the exception, and returns the response object
    
    :param e: The exception that was raised
    :return: A response object
    """
    logger.exception(e)
    response = jsonify({
        "status": e.status_code,
        "msg": e.error
    })
    response.status_code = e.status_code
    return response


@errors_bp.app_errorhandler(ForbiddenError)
def forbidden_exception(e):
    """
    It takes an exception as an argument, logs it, and returns a JSON response with the status code and
    error message
    
    :param e: The exception that was raised
    :return: A response object.
    """
    logger.exception(e)
    response = jsonify({
        "status": e.status_code,
        "msg": e.error
    })
    response.status_code = e.status_code
    return response


@errors_bp.app_errorhandler(GenerateError)
def generate_exception(e):
    """
    It takes an exception object, logs it, and returns a JSON response with the exception's status code,
    message, and errors.
    
    :param e: The exception that was raised
    :return: A function that takes an exception as an argument and returns a response.
    """
    logger.exception(e)
    response = jsonify({
        "status": e.status_code,
        "msg": e.message,
        "errors": e.errors
    })
    response.status_code = e.status_code
    return response


@errors_bp.app_errorhandler(NotFoundError)
def forbidden_exception(e):
    """
    It takes an exception as an argument, logs it, and returns a JSON response with the status code and
    error message
    
    :param e: The exception that was raised
    :return: The response is a JSON object with the status code and the error message.
    """
    logger.exception(e)
    response = jsonify({
        "status": e.status_code,
        "msg": e.error
    })
    response.status_code = e.status_code
    return response


@errors_bp.app_errorhandler(MethodNotAllowed)
def method_exception(e):
    """
    It takes an exception as an argument, logs the exception, and returns a response with a status code
    of 405
    
    :param e: The exception that was raised
    :return: A response object
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.METHOD_NOT_ALLOWED,
            "msg": "Method not Allowed"
        })
    response.status_code = HTTPStatus.METHOD_NOT_ALLOWED
    return response


@errors_bp.app_errorhandler(sqlalchemy.exc.InternalError)
def sql_error(e):
    """
    It takes an exception as an argument, logs it, and returns a JSON response with the error message
    
    :param e: The exception object
    :return: A response object.
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": "Erro de SQL: {}".format(e.orig.args[1])
        })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@errors_bp.app_errorhandler(werkzeug.exceptions.BadRequest)
def bad_request(e):
    """
    It takes an exception as an argument, logs it, and returns a response with a status code of 500
    
    :param e: The exception that was raised
    :return: A response object.
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.BAD_REQUEST,
            "msg": "O navegador não conseguiu visualizar o json."
        })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@errors_bp.app_errorhandler(KeyError)
def key_error(e):
    """
    If there's a KeyError, log the exception and return a JSON response with a status code of 500.
    
    :param e: The exception that was raised
    :return: A response object.
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": "Erro interno! Está faltando o campo: {}".format(e)
        })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@errors_bp.app_errorhandler(NameError)
def name_error(e):
    """
    It takes an exception as an argument, logs the exception, and returns a JSON response with the
    exception message
    
    :param e: The exception that was raised
    :return: The response is being returned.
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": e.args[0]
        })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response


@errors_bp.app_errorhandler(Exception)
def exception(e):
    """
    It takes an exception as an argument, logs it, and returns a JSON response with a status code of 500
    
    :param e: The exception that was raised
    :return: The response is being returned.
    """
    logger.exception(e)
    response = jsonify(
        {
            "status": HTTPStatus.INTERNAL_SERVER_ERROR,
            "msg": "Algo deu Errado! Tente novamente mais tarde!"
        })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    return response
