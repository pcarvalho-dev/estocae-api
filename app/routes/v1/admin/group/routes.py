from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import crud_group
from app.services.errors.default_errors import treated_errors

from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

group_bp = Blueprint("group", __name__, url_prefix='/groups')


@group_bp.route('', methods=['GET', 'POST'])
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
               items: GroupSchema
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
            schema: GroupSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: GroupSchema
      tags:
          - Admin
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_group.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_group.post(schema=True)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@group_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
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
      description: Group
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: GroupSchema
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
            schema: Group
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: GroupSchema
      tags:
          - Admin

    delete:
      security:
      - jwt: []
      parameters:
      - path_params_default
      description: Group
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: GroupSchema
      tags:
          - Admin
    """
    try:
        if request.method == 'GET':
            item = crud_group.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_group.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_group.delete(item_id)
            return default_return(204, 4)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
