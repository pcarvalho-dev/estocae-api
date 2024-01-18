from app.routes.v1 import admin, client, public
from app.routes.v1.routes import v1_bp


def init_app(app):
    admin.init_app(v1_bp)
    client.init_app(v1_bp)
    public.init_app(v1_bp)
    app.register_blueprint(v1_bp)
