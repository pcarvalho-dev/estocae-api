from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app import models
from app.controllers import crud_product_affiliate
from app.controllers.product import crud_product
from app.services.errors.default_errors import treated_errors
from app.services.errors.exceptions import GenerateError, NotFoundError
from app.services.requests.requests import default_return

client_product_bp = Blueprint(
    "client_product", __name__, url_prefix='/products')


@client_product_bp.route('', methods=['GET', 'POST'])
@jwt_required()
def item_multi_routes():
    try:
        user_id = get_jwt_identity()['user_id']
        if request.method == 'POST':
            extra_fields = [('user_id', user_id)]
            item = crud_product.post(schema=True,
                                     extra_fields=extra_fields)
            return default_return(201, 1, item)
        if request.method == 'GET':
            extra_filters = [('status', 'eq', 'active')]
            items, items_paginate = crud_product.get_multi(
                True,
                extra_filters=extra_filters
            )
            return default_return(200, 2, items, items_paginate)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_product_bp.route('/my_products', methods=['GET'])
@jwt_required()
def item_my_products():
    try:
        user_id = get_jwt_identity()['user_id']
        if request.method == 'GET':
            extra_filters = [('user_id', 'eq', user_id)]
            items, items_paginate = crud_product.get_multi(
                True,
                extra_filters=extra_filters
            )
            return default_return(200, 2, items, items_paginate)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_product_bp.route('/<item_id>', methods=['GET', 'PUT'])
@jwt_required()
def item_routes(item_id):
    try:
        if request.method == 'GET':
            item = crud_product.get(item_id, True)
            return default_return(200, 2, item)
        if request.method == 'PUT':
            item = crud_product.update_product(item_id)
            return default_return(200, 3, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_product_bp.route('/<item_id>/affiliate', methods=['POST'])
@jwt_required()
def item_affiliate(item_id):
    try:
        user_id = get_jwt_identity()['user_id']
        if request.method == 'POST':
            item = crud_product.get(item_id)
            if not item:
                raise NotFoundError("Item not found", 404)
            is_affiliate = models.ProductAffiliate.query.filter(
                models.ProductAffiliate.user_id == user_id,
                models.ProductAffiliate.product_id == item_id,
                models.ProductAffiliate.status.in_(['pending', 'approved'])
            ).first()
            if is_affiliate:
                raise GenerateError(
                    409,
                    "Você já tem uma solicitação de afiliação em andamento!"
                )
            crud_product_affiliate.post(
                dict_body={
                    "user_id": user_id,
                    "product_id": item_id
                }
            )
            return default_return(200, 2, "Solicitação de afiliação enviada!")
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
