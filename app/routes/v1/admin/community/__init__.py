from app.routes.v1.admin.community.routes import community_bp


def init_app(admin_bp):
    """
    It takes the admin blueprint and registers the community blueprint to it
    
    :param admin_bp: The blueprint that the community blueprint will be registered to
    """
    admin_bp.register_blueprint(community_bp)
