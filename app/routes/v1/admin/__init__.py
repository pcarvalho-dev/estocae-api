from app.routes.v1.admin import city, country, group, state, user, community, \
    main, terms_and_conditions
from app.routes.v1.admin.routes import admin_bp


def init_app(v1_bp):
    """
    It registers the admin_bp blueprint to the v1_bp blueprint
    
    :param v1_bp: The blueprint for the version 1 of the API
    """
    main.init_app(admin_bp)
    country.init_app(admin_bp)
    state.init_app(admin_bp)
    city.init_app(admin_bp)
    group.init_app(admin_bp)
    user.init_app(admin_bp)
    terms_and_conditions.init_app(admin_bp)
    community.init_app(admin_bp)
    v1_bp.register_blueprint(admin_bp)
