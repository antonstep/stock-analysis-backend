import os
from flask import Flask
from flask_cors import CORS
from .routes import main
from .errors import errors
from config import Config

def create_app():
    """
    Create and configure an instance of the Flask application.
    
    Sets up the Flask application with configuration from the Config class,
    registers necessary blueprints, and configures CORS with environment-specific allowed origins.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Set up CORS with support for credentials and dynamic origin support
    allowed_origins = os.getenv('ALLOWED_ORIGINS', '*').split(',')
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": ["https://stock-analysis-frontend.vercel.app/"]}})

    return app