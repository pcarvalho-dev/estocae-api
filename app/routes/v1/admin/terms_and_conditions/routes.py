from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.terms_and_conditions import crud_terms_and_conditions
from app.services.errors.default_errors import treated_errors
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

terms_and_conditions_bp = Blueprint('terms_and_conditions', __name__, url_prefix="/terms_and_conditions")


@terms_and_conditions_bp.route('', methods=['GET', 'POST'])
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
          description: Query made successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Admin Terms and Conditions

    post:
      security:
      - jwt: []
      requestBody:
        required: true
        content:
          application/json:
            schema: TermsAndConditionsSchema
            examples:
              for privacy policy:
                value:
                  title: Título do Termo
                  content: Conteúdo dos termos e condições
                  document_type: PRIVACY_POLICY
              for terms of use:
                value:
                  title: Título do Termo
                  content: Conteúdo dos termos e condições
                  document_type: TERMS_OF_USE
      responses:
        '201':
          description: Registered successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Admin Terms and Conditions
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_terms_and_conditions.get_multi(schema=True)
            return default_return(200, 2, items, items_paginate)
        if request.method == 'POST':
            item = crud_terms_and_conditions.post(schema=True)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@terms_and_conditions_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
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
      responses:
        '200':
          description: Query made successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Admin Terms and Conditions

    put:
      security:
      - jwt: []
      parameters:
      - path_params_default
      requestBody:
        required: true
        content:
          application/json:
            schema: TermsAndConditionsSchema
            example:
              title: Termos e Condições Atualizado
              content: Atualizar conteúdo de Termos e Condições
      responses:
        '200':
          description: Updated successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Admin Terms and Conditions

    delete:
      security:
      - jwt: []
      parameters:
      - path_params_default
      responses:
        '200':
          description: Deleted successfully
      tags:
          - Admin Terms and Conditions
    """
    try:
        if request.method == 'GET':
            item = crud_terms_and_conditions.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_terms_and_conditions.update_terms_and_conditions(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_terms_and_conditions.delete_terms_and_conditions(item_id)
            return default_return(200, 4)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@terms_and_conditions_bp.route('<item_id>/publish', methods=['PATCH'])
@jwt_required()
@intercept_admin_user
def item_multi_publish_routes(item_id):
    """
    ---
    patch:
      security:
      - jwt: []
      parameters:
      - path_params_default

      responses:
        '201':
          description: Registered successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Admin Terms and Conditions
    """
    try:
        if request.method == 'PATCH':
            msg = crud_terms_and_conditions.publish_terms_and_conditions(item_id=item_id)
            return default_return(201, 1, msg)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
