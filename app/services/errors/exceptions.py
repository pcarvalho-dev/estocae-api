import logging
from http import HTTPStatus

logger = logging.getLogger(__name__)


class BadRequestError(Exception):
    """
    Exception raised when request data is incorrect.
    status code: 400
    """

    def __init__(self, message="Bad request sintaxe ou método não suportado",
                 status_code=HTTPStatus.BAD_REQUEST):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


class UnauthorizedError(Exception):
    def __init__(self, error, status_code=HTTPStatus.UNAUTHORIZED):
        """
        This function is used to raise an exception when the user is not authorized to access the resource
        
        :param error: The error message to be returned to the user
        :param status_code: The HTTP status code to return
        """
        Exception.__init__(self)
        self.error = error
        self.status_code = status_code


class ForbiddenError(Exception):
    def __init__(self, error='Recurso não encontrado',
                 status_code=HTTPStatus.FORBIDDEN):
        """
        It's a function that takes in an error message and a status code, and returns an error message and a
        status code
        
        :param error: The error message that will be returned to the user, defaults to Recurso não
        encontrado (optional)
        :param status_code: The HTTP status code to return
        """

        Exception.__init__(self)
        self.error = error
        self.status_code = status_code


class NotFoundError(Exception):
    def __init__(self, message="Recurso não encontrado",
                 status_code=HTTPStatus.NOT_FOUND):
        """
        It's a function that takes in an error message and a status code, and returns an error message and a
        status code

        :param error: The error message that will be returned to the user, defaults to Recurso não
        encontrado (optional)
        :param status_code: The HTTP status code that will be returned to the client
        """

        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


class GenerateError(Exception):
    """Generate generic error"""

    def __init__(self, error, status_code=500, errors=[]):
        """
        This function is a constructor that takes in an error message, a status code, and a list of errors.
        It then sets the message, status code, and errors to the values passed in
        
        :param error: The error message
        :param status_code: The HTTP status code, defaults to 500 (optional)
        :param errors: A list of errors that are related to the error
        """
        self.message = error
        self.status_code = status_code
        self.errors = errors
        super().__init__(self.message, self.errors)


class DuplicateKey:
    def __init__(self, error):
        self.error = error

    def response(self):
        make_split = self.error.split(" ")
        value = make_split[2]
        key = make_split[5]

        if key == "'doc_value'":
            key = 'cpf'

        response = f'Erro. Já existe um usuário com {key}: {value}, cadastrado no sistema'

        return response


class ConflictError(Exception):
    """
    Exception raised when entity is in conflict with an existing entity.
    status code: 409
    """

    def __init__(self, message="Conflito", status_code=HTTPStatus.CONFLICT):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
