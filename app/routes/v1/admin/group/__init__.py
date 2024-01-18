from app.routes.v1.admin.group.routes import group_bp


def init_app(admin_bp):
    """
    It registers the blueprint with the admin blueprint
    
    :param admin_bp: The blueprint that the admin blueprint is registered to
    """
    admin_bp.register_blueprint(group_bp)
