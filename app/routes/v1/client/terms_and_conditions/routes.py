from flask import request, Blueprint

from app.controllers.terms_and_conditions import crud_terms_and_conditions
from app.controllers.user_terms_and_conditions import crud_user_terms_and_conditions
from app.services.errors.default_errors import treated_errors
from app.services.requests.requests import default_return

client_terms_and_conditions_bp = Blueprint('terms_and_conditions', __name__, url_prefix="/terms_and_conditions")


@client_terms_and_conditions_bp.route('', methods=['GET', 'POST'])
def item_multi_routes():
    """
    ---
    get:
      parameters:
        - in: query
          name: document_type
          description: filter document type
          required: true
          schema:
            type: string
            enum: [PRIVACY_POLICY, TERMS_OF_USE]
      responses:
        '200':
          description: Query made successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Client Terms and Conditions

    post:
      requestBody:
        required: true
        content:
          application/json:
            schema: UserTermsAndConditionsSchema
            example:
                user_id: 2
      responses:
        '201':
          description: Registered successfully
          content:
            application/json:
              schema: TermsAndConditionsSchema
      tags:
          - Client Terms and Conditions
    """
    try:
        if request.method == 'GET':
            document_type = request.args.get('document_type')

            if document_type:
                items = crud_user_terms_and_conditions.list_terms_and_conditions_to_agree()
                return default_return(200, 2, items)
            else:
                extra_filters = [('status', 'eq', 'PUBLISHED')]
                items, items_paginate = crud_terms_and_conditions.get_multi(True,
                                                                extra_filters=extra_filters)
                return default_return(200, 2, items, items_paginate)
        if request.method == 'POST':
            item = crud_user_terms_and_conditions.agree_terms_and_conditions()
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
