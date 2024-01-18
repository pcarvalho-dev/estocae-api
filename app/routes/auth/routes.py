from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.controllers.auth import auth_login, auth_refresh

from app.services.errors.exceptions import UnauthorizedError
from app.services.requests.requests import default_return

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")


@auth_bp.route('/token', methods=["POST"])
def token():
    """
    ---
    post:
      security:
        - api_key: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: TokenSchema
            example:
              username: administrador@mailinator.com
              password: "123456"
              grant_type: password
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: TokenSchema
      tags:
          - Token
    """
    try:
        return auth_login()
    except UnauthorizedError as e:
        return default_return(e.status_code, {"Error": str(e.error)})
    except Exception as e:
        return {"Error": str(e)}, 500


@auth_bp.route('/refresh', methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    try:
        user_jwt = get_jwt_identity()
        return auth_refresh(user_jwt)
    except UnauthorizedError as e:
        return {"Error": str(e)}, 401
    except Exception as e:
        return {"Error": str(e)}, 500
