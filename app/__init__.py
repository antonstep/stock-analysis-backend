from flask import Flask
from flask_cors import CORS
from .routes import main
from .errors import errors
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registering blueprints
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Set up CORS with dynamic origin support
    allowed_origins = os.getenv('ALLOWED_ORIGINS', 'https://stock-analysis-frontend.vercel.app').split(',')
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": allowed_origins}})

    return app