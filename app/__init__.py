# In app/__init__.py
from flask import Flask
from .routes import main
from .errors import errors

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app
