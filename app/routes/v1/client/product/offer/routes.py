from app import schemas
from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_offer
from app.controllers.product import crud_product
from app.services.errors.default_errors import treated_errors
from app.services.errors.exceptions import NotFoundError
from app.services.requests.requests import default_return

offer_bp = Blueprint("offer", __name__, url_prefix='/<product_id>/offers')


@offer_bp.route('', methods=['GET', 'POST'])
@jwt_required()
def item_multi_routes(product_id):
    try:
        product = crud_product.get(product_id)
        if not product:
            raise NotFoundError()
        extra_filters = []
        if request.method == 'GET':
            extra_filters.append(('product_id', 'eq', product_id))
            items, items_paginate = crud_offer.get_multi(
                extra_filters=extra_filters,
                schema=True
            )
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            extra_fields = [('product_id', product_id)]
            item = crud_offer.post(extra_fields=extra_fields)
            item.url = f"/{item.hash_id}"
            item.update()
            item = schemas.OfferSchema().dump(item)
            return default_return(201, 1, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@offer_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def item_routes(product_id, item_id):
    try:
        product = crud_product.get(product_id)
        if not product:
            raise NotFoundError()
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
