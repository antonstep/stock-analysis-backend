import sys
import os
import pytest

# Adjust Python path to include the parent directory where the app package resides
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # Import the Flask application

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create a Flask app using the testing configuration
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgres://stock_analysis_backend_user:87UcUha5aNxtWZPQ9fLtPmzE2HgRUVnc@dpg-cpcblovjbltc73ac7ngg-a/stock_analysis_backend"  # Use in-memory SQLite for tests
    })

    # Push an application context before running the tests
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
