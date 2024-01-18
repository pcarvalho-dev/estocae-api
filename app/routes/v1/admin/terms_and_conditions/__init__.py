from .routes import terms_and_conditions_bp


def init_app(admin_bp):
    admin_bp.register_blueprint(terms_and_conditions_bp)
