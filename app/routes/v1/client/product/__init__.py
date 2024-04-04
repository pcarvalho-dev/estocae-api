from app.routes.v1.client.product.routes import client_product_bp

from . import checkout, coupon, offer, page


def init_app(admin_bp):
    """
    It registers the blueprint with the admin blueprint

    :param admin_bp: The blueprint that the admin blueprint is registered to
    """
    coupon.init_app(client_product_bp)
    offer.init_app(client_product_bp)
    checkout.init_app(client_product_bp)
    page.init_app(client_product_bp)
    admin_bp.register_blueprint(client_product_bp)
