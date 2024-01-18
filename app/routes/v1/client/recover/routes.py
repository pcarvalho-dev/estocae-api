from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from app.controllers.user_recover_pass_with_code import RecoverPassWithCode
from app.services.errors.default_errors import treated_errors
from app.services.errors.exceptions import DuplicateKey
from app.services.requests.requests import default_return

recover_pass_bp = Blueprint('public_recover_pass', __name__, url_prefix="/recover")


@recover_pass_bp.route('', methods=['POST'])
def item_multi_routes():
    """
    ---
    post:
      parameters:
        - in: query
          name: type_token
          required: True
          description: Type token
          schema:
            type: string
            enum: [hash_code]
      requestBody:
        required: true
        content:
          application/json:
            schema: ReturnEmail
            examples:
              with email:
                value:
                  username: userteste@email.com
              with cellphone:
                value:
                  username: (00) 00000-0000
      responses:
        '200':
          description: Code successfully sent
          content:
            application/json:
              schema: ReturnEmail

      tags:
          -  Client
    """

    try:

        if request.method == 'POST':
            type_token = request.args.get("type_token", type=str)
            username = request.get_json()['username']
            email = None
            if type_token == 'hash_code':
                email = RecoverPassWithCode(username=username).recover()
            return default_return(200, 'Code successfully sent', {"email": email})

    except IntegrityError as e:
        error = str(e.__dict__['orig'].args[1])
        message = DuplicateKey(error=error).response()
        return default_return(400, 'Bad Request', {"Error": str(message)})
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@recover_pass_bp.route('/code', methods=['POST'])
def item_validate_code():
    """
    ---
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema: CheckCode
            example:
              email: userteste@email.com
              code: "123456"
      responses:
         '200':
          description: Successfully validated code
          content:
            application/json:
              schema: ReturnTokenUpdate

      tags:
          -  Client
    """
    try:

        if request.method == 'POST':
            dict_body = request.get_json()
            token_update = RecoverPassWithCode().validate_code(dict_body=dict_body)
            return default_return(200, 'Successfully validated code', token_update)

    except IntegrityError as e:
        error = str(e.__dict__['orig'].args[1])
        message = DuplicateKey(error=error).response()
        return default_return(400, 'Bad Request', {"Error": str(message)})
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@recover_pass_bp.route('/reset', methods=['POST'])
def item_confirm():
    """
    ---
    post:
      parameters:
        - in: query
          name: type_token
          required: True
          description: Type token
          schema:
            type: string
            enum: [hash_code]
      requestBody:
        required: true
        content:
          application/json:
            schema: RegisterNewPass
            example:
              email: userteste@email.com
              password: "123456"
              token_update: "5858c9e4-18b2-11ed-bb4c-0242ac170004"
      responses:
        '200':
          description: Password change successfully

      tags:
          -  Client
    """
    try:

        if request.method == 'POST':
            type_token = request.args.get("type_token", type=str)
            dict_body = request.get_json()
            if type_token == 'hash_code':
                RecoverPassWithCode().reset_pass(dict_body=dict_body)
            return default_return(200, 'Password change successfully', {})

    except IntegrityError as e:
        error = str(e.__dict__['orig'].args[1])
        message = DuplicateKey(error=error).response()
        return default_return(400, 'Bad Request', {"Error": str(message)})
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
