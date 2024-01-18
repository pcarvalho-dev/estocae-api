import os
from apispec import APISpec
import warnings
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

# Creating a spec object.
from app.services.apispec.default_params import DefaultParameters

spec = APISpec(
    title=os.environ.get('PROJECT_NAME'),
    version=os.environ.get('PROJECT_VERSION'),
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Defining the security scheme for the API.
api_key_scheme = {"type": "apiKey", "in": "header", "name": "Authorization",
                  "description": f"Authorization teste para sistema e admin: {os.environ.get('ADMIN_BASIC')}"
                                 f"\n\n Authorization teste para cliente: {os.environ.get('CLIENT_BASIC')}"}
# Defining the security scheme for the API.
jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

spec.components.security_scheme("api_key", api_key_scheme)
spec.components.security_scheme("jwt", jwt_scheme)

DefaultParameters(spec=spec).active_params_default()


def init_app(app):
    """
    It takes the Flask app object and registers all the functions in the app.view_functions dictionary
    with the swagger spec
    
    :param app: the flask app
    """
    with app.test_request_context():
        # register all swagger documented functions here
        for fn_name in app.view_functions:
            if fn_name == 'static':
                continue
            # print(f"Loading swagger docs for function: {fn_name}")
            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)


warnings.filterwarnings(
    "ignore",
    message="Multiple schemas resolved to the name "
)
