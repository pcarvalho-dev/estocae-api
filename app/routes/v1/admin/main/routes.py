from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_main_settings
from app.controllers.main_company import crud_main_company
from app.services.errors.default_errors import treated_errors
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

main_bp = Blueprint("main", __name__, url_prefix='/main')


@main_bp.route('', methods=['GET', 'PUT'])
@jwt_required()
@intercept_admin_user
def item_multi_routes():
    """
    ---
    get:
      security:
        - jwt: []
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainCompanySchema
      tags:
          - Admin Main Company

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MainCompanySchema
            example:
              name: Companhia X
              email: compania@teste.com
              email_notification: compania@teste.com
              cell_phone: (99) 99999-9999
              landline: (99) 39999-9999
              status: True
              enable_notification_host: True
              ein: "28.787.336/0001-65"
              company_name: Company Name Ltda
              facebook: companyfacebook
              instagram: companyinstagram
              app_android: companyandroid
              app_ios: companyios
              address:
                code_post: '74210-010'
                street: 'Av. T-2'
                number: 'S/N'
                district: St. Bueno
                complement: QD 98 LT 6
                city_id: 971
      responses:
        '200':
          description: Updated successfully
          content:
            application/json:
              schema: MainCompanySchema
      tags:
          - Admin Main Company
    """
    try:
        if request.method == 'GET':
            item = crud_main_company.get_first(schema=True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_main_company.update_company(schema=True)
            return default_return(200, 3, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@main_bp.route('/settings', methods=['GET', 'PUT'])
@jwt_required()
@intercept_admin_user
def item_configuration_routes():
    """
    ---
    get:
      security:
        - jwt: []
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainSettingsSchema
      tags:
          - Admin

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MainSettingsSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainSettingsSchema
      tags:
          - Admin
    """
    try:
        if request.method == 'GET':
            item = crud_main_settings.get_first(schema=True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_main_settings.put_first(True)
            return default_return(200, 3, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
