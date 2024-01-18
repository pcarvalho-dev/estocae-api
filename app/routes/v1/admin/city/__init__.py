from .routes import city_bp


def init_app(admin_bp):
    admin_bp.register_blueprint(city_bp)
