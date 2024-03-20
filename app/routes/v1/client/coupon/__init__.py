from app.routes.v1.client.coupon.routes import coupon_bp


def init_app(client_bp):
    """
    It registers the blueprint with the admin blueprint

    :param client_bp: The blueprint that the admin blueprint is registered to
    """
    client_bp.register_blueprint(coupon_bp)
