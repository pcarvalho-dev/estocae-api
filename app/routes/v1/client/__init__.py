from . import coupon, offer, plan, product, recover, terms_and_conditions
from .routes import client_bp


def init_app(v1_bp):
    coupon.init_app(client_bp)
    recover.init_app(client_bp)
    terms_and_conditions.init_app(client_bp)
    product.init_app(client_bp)
    plan.init_app(client_bp)
    offer.init_app(client_bp)
    v1_bp.register_blueprint(client_bp)
