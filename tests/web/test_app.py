"""Test App"""
from web.app import create_app


class TestApp:
    """Test App"""

    def test_create_app(self):
        """Test create_app"""
        assert create_app("testing").testing
