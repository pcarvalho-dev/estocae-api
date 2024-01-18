from app.routes import auth, docs, v1, errors


def init_app(app):
    auth.init_app(app)
    docs.init_app(app)
    errors.init_app(app)
    v1.init_app(app)

