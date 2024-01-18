from .routes import country_bp


def init_app(admin_bp):
    """
    It registers the country_bp blueprint with the admin_bp blueprint
    
    :param admin_bp: The blueprint that the admin blueprint is registered to
    """
    admin_bp.register_blueprint(country_bp)
