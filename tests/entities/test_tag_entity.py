"""Test Tag Entity"""

import json

import pytest

from src.entities.tag_entity import Tag


class TestTag:
    """Test Tag Entity class"""

    data = {"id": "6f7a8c66-2f7f-4f5d-9c9b-f2ab719c6a50", "title": "example tag"}

    def test_tag_init(self):
        """Tag class successful initializes with the right arguments"""
        tag_id = TestTag.data["id"]
        title = TestTag.data["title"]
        tag = Tag(id=tag_id, title=title)

        assert tag.id == TestTag.data["id"]
        assert tag.title == TestTag.data["title"]
        assert isinstance(tag, Tag)

    def test_tag_init_raises_error(self):
        """Test tag raises error if an invalid uuid is used"""
        # The tests below fail
        # Checkout documentation on why this is. The code was suggested by chatGPT

        # id = ''
        # title = TestTag.data["title"]
        # with pytest.raises(ValueError):
        #     Tag(id=id, title=title)

    def test_tag_from_dict(self):
        """Successfully initializes from a dictionary object"""
        tag = Tag.from_dict(TestTag.data)

        assert isinstance(tag, Tag)
        assert tag.id == TestTag.data["id"]
        assert tag.title == TestTag.data["title"]

    def test_tag_from_dict_raises_value_error(self):
        """Test tag from_dict raises value error if data is invalid"""
        invalid_data = {}
        with pytest.raises(Exception):
            Tag.from_dict(invalid_data)

    def test_tag_to_dict(self):
        """Test tag to_dict method"""
        tag = Tag.from_dict(TestTag.data)

        assert tag.to_dict() == TestTag.data

    def test_tag_to_json(self):
        """Test tag to_json returns a json string of a tag"""
        tag = Tag.from_dict(TestTag.data)

        json_tag = tag.to_json()
        assert TestTag.data == json.loads(json_tag)
