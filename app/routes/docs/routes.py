import warnings

from flask import jsonify, render_template, Blueprint

from app.services import spec

docs_bp = Blueprint('docs', __name__, url_prefix="/docs")


warnings.filterwarnings(
    "ignore",
    message="Multiple schemas resolved to the name ",
    category=UserWarning

)

@docs_bp.route('/api/swagger.json')
def create_swagger_spec():
    """
    It takes the spec object that we created earlier and converts it to a dictionary
    :return: The swagger spec is being returned as a JSON object.
    """
    return jsonify(spec.to_dict())


@docs_bp.route('')
def swagger_docs():
    """
    It renders the swagger/index.html template, which is the swagger UI, and passes in the base_url
    variable, which is the URL of the swagger.json file
    :return: The swagger_docs() function is returning the render_template() function.
    """
    return render_template('/swagger/index.html', base_url='docs')
