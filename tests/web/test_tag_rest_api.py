"""Test Tag Rest API"""


class TestTagRestAPI:
    """Test Tag REST API"""

    def test_tag_end_point(self, client):
        """Test End"""
        http_response = client.get("/")

        assert http_response.status_code == 200
        assert http_response.data == b"Hello World!"
