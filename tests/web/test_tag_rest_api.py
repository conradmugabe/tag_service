"""Test Tag Rest API"""
from web.app import create_app


class TestTagRestAPI:
    """Test Tag REST API"""

    def test_create_app(self):
        """Test create app"""
        assert create_app("testing").testing

    def test_tag_end_point(self, client):
        """Test End"""
        http_response = client.get("/")

        assert http_response.status_code == 200
        assert http_response.data == b"Hello World!"
