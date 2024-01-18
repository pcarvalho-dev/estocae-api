from app.routes.v1.admin.state.routes import state_bp


def init_app(app):
    """
    It registers the state_bp blueprint with the app
    
    :param app: The Flask application instance
    """
    app.register_blueprint(state_bp)
