from .routes import docs_bp


def init_app(app):
    """
    It registers the blueprint with the Flask application
    
    :param app: The Flask application instance
    """
    app.register_blueprint(docs_bp)
