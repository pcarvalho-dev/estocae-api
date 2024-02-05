from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_product
from app.services.errors.default_errors import treated_errors
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

product_bp = Blueprint("product", __name__, url_prefix='/products')


@product_bp.route('', methods=['GET', 'POST'])
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
               items: ProductSchema
      tags:
          - Admin Product

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: ProductSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ProductSchema
      tags:
          - Admin Product
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_product.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_product.post(schema=True)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@product_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
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
              schema: ProductSchema
      tags:
          - Admin Product

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
              schema: ProductSchema
      tags:
          - Admin Product

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
              schema: ProductSchema
      tags:
          - Admin Product
    """
    try:
        if request.method == 'GET':
            item = crud_product.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_product.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_product.delete(item_id)
            return default_return(204, 4)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
