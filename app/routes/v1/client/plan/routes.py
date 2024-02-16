from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app import models

from app.controllers import crud_plan
from app.services.errors.default_errors import treated_errors
from app.services.errors.exceptions import GenerateError
from app.services.requests.requests import default_return
from flask_jwt_extended import get_jwt_identity

client_plan_bp = Blueprint(
    "client_plan", __name__, url_prefix='/plans')


@client_plan_bp.route('', methods=['GET'])
@jwt_required()
def item_multi_routes():
    try:
        if request.method == 'GET':
            items, items_paginate = crud_plan.get_multi(True)
            return default_return(200, 2, items, items_paginate)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_plan_bp.route('/<item_id>', methods=['GET'])
@jwt_required()
def item_routes(item_id):
    try:
        if request.method == 'GET':
            item = crud_plan.get(item_id, True)
            return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@client_plan_bp.route('/<item_id>/subscribe', methods=['POST'])
@jwt_required()
def item_subscribe(item_id):
    try:
        user_id = get_jwt_identity()['user_id']
        if request.method == 'POST':
            item = crud_plan.get(item_id, True)
            if not item:
                raise GenerateError("Plan not found", 404)
            models.UserPlan(
                user_id=user_id,
                plan_id=item_id
            ).save()
            return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
