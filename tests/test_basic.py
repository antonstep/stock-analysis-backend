# In tests/test_basic.py
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_world(client):
    """Test the hello world route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}
