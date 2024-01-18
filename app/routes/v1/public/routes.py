from flask import Blueprint

from app.controllers.main_company import crud_main_company
from app.controllers import crud_main_settings
from app.services.errors.default_errors import treated_errors
from app.services.requests.requests import default_return

public_bp = Blueprint('public_bp', __name__, url_prefix="/public")


@public_bp.route('/main', methods=['GET', 'POST'])
def item_main():
    """
    ---
    get:
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainCompanySchema
      tags:
          - Public

    """
    try:
        item = crud_main_company.get_first(schema=True)
        return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e


@public_bp.route('/main/settings', methods=['GET', 'POST'])
def item_settings():
    """
    ---
    get:
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainSettingsSchema
      tags:
          - Public

    """
    try:
        item = crud_main_settings.get_first(schema=True)
        return default_return(200, 2, item)
    except treated_errors as e:
        return default_return(e.status_code, e.message, {"Error": str(e)})
    except Exception as e:
        raise e
