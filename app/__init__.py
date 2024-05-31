# In app/__init__.py
import os
from flask import Flask
from flask_cors import CORS

# Local imports
from .routes import main
from .errors import errors
from config import Config

def create_app():
    """
    Create and configure an instance of the Flask application.
    
    This function sets up the Flask application with configurations, registers
    necessary blueprints, and configures CORS based on environment-specific
    allowed origins.
    """
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Register blueprint for main routes
    app.register_blueprint(main)
    # Register blueprint for handling errors
    app.register_blueprint(errors)

    # Setup CORS with dynamic origin support
    # Retrieve allowed origins from environment variable; default is '*'
    allowed_origins = os.getenv('ALLOWED_ORIGINS', '*').split(',')
    # Configure CORS for the application with allowed origins for all routes under '/api/*'
    CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

    return app