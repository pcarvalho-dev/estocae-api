from .routes import client_terms_and_conditions_bp


def init_app(app):
    app.register_blueprint(client_terms_and_conditions_bp)
