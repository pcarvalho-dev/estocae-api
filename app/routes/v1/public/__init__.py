from .routes import public_bp


def init_app(v1_bp):
    v1_bp.register_blueprint(public_bp)
