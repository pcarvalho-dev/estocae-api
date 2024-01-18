from .handlers import errors_bp


def init_app(app):
    """
    It registers the blueprint with the application
    
    :param app: The Flask application instance
    """
    app.register_blueprint(errors_bp)
