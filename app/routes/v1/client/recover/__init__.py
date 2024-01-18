from .routes import recover_pass_bp


def init_app(app):
    app.register_blueprint(recover_pass_bp)
