from app import create_app
from waitress import serve
import os

# Creating the app.
app = create_app()

# Getting the port from the environment variable PORT or API_PORT.
port = os.environ.get('PORT', os.environ.get('API_PORT'))

# This is a way to run the app in production or development mode.
if __name__ == "__main__":
    if os.environ.get('APP_ENV', 'development') == "production":
        app.logger.info('Environment prod running. Port %s', port)
        serve(app, host="0.0.0.0", port=port)
    else:
        app.run(debug=True, host='0.0.0.0', port=port)