from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import crud_state
from app.services.errors.default_errors import treated_errors
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

state_bp = Blueprint('state', __name__, url_prefix="/states")


@state_bp.route('', methods=['GET', 'POST'])
@jwt_required()
@intercept_admin_user
def item_multi_routes():
    """
    ---
    get:
      security:
        - jwt: []
      parameters:
        - page_param
        - per_page_param
        - search_param
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema:
               type: array
               items: StateSchema
      tags:
          - Admin

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: StateSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: StateSchema
      tags:
          - Admin
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_state.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_state.post(schema=True)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@state_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
      - jwt: []
      parameters:
      - path_params_default
      description: State
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: StateSchema
      tags:
          - Admin

    put:
      security:
      - jwt: []
      parameters:
      - path_params_default
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: StateSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: StateSchema
      tags:
          - Admin

    delete:
      security:
      - jwt: []
      parameters:
      - path_params_default
      description: State
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: StateSchema
      tags:
          - Admin
    """
    try:
        if request.method == 'GET':
            item = crud_state.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_state.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_state.delete(item_id)
            return default_return(204, 4)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
