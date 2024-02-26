from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_offer
from app.services.errors.default_errors import treated_errors
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

offer_bp = Blueprint("offer", __name__, url_prefix='/offers')


@offer_bp.route('', methods=['GET', 'POST'])
@jwt_required()
@intercept_admin_user
def item_multi_routes():
    try:
        if request.method == 'GET':
            items, items_paginate = crud_offer.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_offer.post(schema=True)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@offer_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    try:
        if request.method == 'GET':
            item = crud_offer.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_offer.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_offer.delete(item_id)
            return default_return(204, 4)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
