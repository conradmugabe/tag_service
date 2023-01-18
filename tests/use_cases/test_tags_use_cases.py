"""Test Tag Use Cases"""

import uuid
from unittest import mock

import pytest

from src.entities.tag_entity import Tag
from src.use_cases.tag_use_cases import TagUseCases


@pytest.fixture()
def tags_list():
    """Tags list"""
    tag1 = Tag(id=uuid.uuid4(), title="tag 1")
    tag2 = Tag(id=uuid.uuid4(), title="tag 2")
    tag3 = Tag(id=uuid.uuid4(), title="tag 3")
    return [tag1, tag2, tag3]


class TestTagUseCases:
    """Test Tag Use Cases"""

    def test_tag_use_cases_init(self):
        """Test tag use cases initialization"""
        repo = mock.Mock()
        tag_use_cases = TagUseCases(database_service=repo)

        assert isinstance(tag_use_cases, TagUseCases)

    def test_tag_list_without_parameters(self, tags_list):
        """Test tag"""
        repo = mock.Mock()
        repo.find_all.return_value = tags_list

        tag_use_cases = TagUseCases(database_service=repo)
        tags = tag_use_cases.get_all()

        repo.find_all.assert_called_once()
        repo.find_all.assert_called_with()
        assert tags == tags_list
