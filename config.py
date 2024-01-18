import datetime
import os

# Setting the environment variables for the Flask app.
try:
    APP_ENV = str(os.environ['APP_ENV'])
except KeyError:
    APP_ENV = 'development'

ROOT = os.path.dirname(os.path.abspath(__file__))
print(ROOT)


class Config:
    # A constant that is used to define the version of the API.
    API_VERSION = "v1"

    # Setting the environment variables for the Flask app.
    SITE_HTTPS = os.environ.get("SITE_HTTPS")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    JSON_SORT_KEYS = False
    WTF_CSRF_CHECK_DEFAULT = False
    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    UPLOAD_FOLDER = f'{ROOT}/static'
    STATIC_FOLDER = f'{ROOT}/static'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    # This is the configuration for JWT.
    JWT_EXPIRES = int(os.environ.get('JWT_EXPIRES'))
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=JWT_EXPIRES)

    # The configuration for AWS.
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET = os.environ.get('AWS_BUCKET')
    AWS_BUCKET_CLOUDFRONT = os.environ.get('AWS_BUCKET_CLOUDFRONT')
    AWS_BUCKET_LOCATION = os.environ.get('AWS_BUCKET_LOCATION')
    AWS_EMAIL_LOCATION = os.environ.get('AWS_EMAIL_LOCATION')
    AWS_EMAIL_SENDER = os.environ.get('AWS_EMAIL_SENDER')

    # Setting up the database connection.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
    SQLALCHEMY_BINDS = {
        "slave": SQLALCHEMY_DATABASE_URI
    }

    # Setting up the cache.
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "simple")
    if CACHE_TYPE == "redis":
        CACHE_REDIS_HOST = os.environ.get("CACHE_REDIS_HOST")
        CACHE_REDIS_PORT = os.environ.get("CACHE_REDIS_PORT")
        CACHE_KEY_PREFIX = SITE_HTTPS
