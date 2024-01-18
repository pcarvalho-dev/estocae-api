import warnings


def init_app(app):
    """
    It ignores the warning that is generated when you have multiple schemas with the same name
    
    :param app: The Flask application object
    """
    warnings.filterwarnings(
        "ignore",
        message="Multiple schemas resolved to the name "
    )
    warnings.filterwarnings(
        "ignore",
        message="Multiple schemas resolved to the name City. The name has been modified. Either manually add each of the schemas with a different name or provide a custom schema_name_resolver.",
    )
    return app
