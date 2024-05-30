# In app/__init__.py
import os
from flask import Flask
from flask_cors import CORS

# Local imports
from .routes import main
from .errors import errors
from config import Config

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Setup CORS with dynamic origin support
    allowed_origins = os.getenv('ALLOWED_ORIGINS', '*').split(',')
    CORS(app, resources={r"/api/*": {"origins": "https://antonstep.github.io/stock-analysis-frontend/"}})  # Adjust for production

    return app
