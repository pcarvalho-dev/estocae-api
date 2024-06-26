from app.routes.v1.client.product.page.routes import product_page_bp


def init_app(client_bp):
    """
    It registers the blueprint with the client blueprint

    :param client_bp: The blueprint that the client blueprint is registered to
    """
    client_bp.register_blueprint(product_page_bp)
