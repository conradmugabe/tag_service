"""pytest conftest"""
import pytest

from web.app import create_app


@pytest.fixture
def app():
    """flask testing app"""
    return create_app("testing")


@pytest.fixture
def client(app):
    """Flask test client"""
    return app.test_client()
