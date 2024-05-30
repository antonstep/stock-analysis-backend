# In app/__init__.py
from flask import Flask
from .routes import main
from .errors import errors
from config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.config.from_object(Config)
    return app
