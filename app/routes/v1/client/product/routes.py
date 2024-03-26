from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_product, crud_product_page
from app.services.errors.default_errors import treated_errors
from app.services.errors.exceptions import NotFoundError
from app.services.requests.requests import default_return
from flask_jwt_extended import get_jwt_identity

client_product_bp = Blueprint(
    "client_product", __name__, url_prefix='/products')


@client_product_bp.route('', methods=['GET'])
def item_multi_routes():
    try:
        if request.method == 'GET':
            items, items_paginate = crud_product.get_multi(True)
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


@client_product_bp.route('/<item_id>', methods=['GET'])
@jwt_required()
def item_routes(item_id):
    try:
        if request.method == 'GET':
            item = crud_product.get(item_id, True)
            return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_product_bp.route('/<item_id>/affiliate', methods=['POST'])
@jwt_required()
def item_affiliate(item_id):
    try:
        user_id = get_jwt_identity()['user_id']
        if request.method == 'GET':
            item = crud_product.get(item_id)
            if not item:
                raise NotFoundError("Item not found", 404)
            item.user_id = user_id
            item.update()
            return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_product_bp.route('/<item_id>/pages', methods=['POST', 'GET'])
@jwt_required()
def item_pages(item_id):
    try:
        if request.method == 'GET':
            extra_filters = [('product_id', 'eq', item_id)]
            items, items_paginate = crud_product_page.get_multi(
                extra_filters=extra_filters,
                schema=True
            )
            return default_return(200, 2, items, items_paginate)
        if request.method == 'POST':
            item = crud_product_page.post(
                extra_fields=[('product_id', item_id)]
            )
            return default_return(201, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
