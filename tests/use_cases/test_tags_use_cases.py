import uuid
from unittest import mock

import pytest

from src.entities.tag_entity import Tag
from src.use_cases.tag_use_cases import TagUseCases


class TestTagUseCases:
    @pytest.fixture()
    def _tags_list(self):
        tag1 = Tag(id=uuid.uuid4(), title="tag 1")
        tag2 = Tag(id=uuid.uuid4(), title="tag 2")
        tag3 = Tag(id=uuid.uuid4(), title="tag 3")
        return [tag1, tag2, tag3]

    def test_tag_use_cases_init(self):
        repo = mock.Mock()
        tag_use_cases = TagUseCases(database_service=repo)

        assert isinstance(tag_use_cases, TagUseCases)

    def test_tag_list_without_parameters(self):
        repo = mock.Mock()
        repo.findAll.return_value = self._tags_list

        tag_use_cases = TagUseCases(database_service=repo)
        tags = tag_use_cases.getAll()

        repo.findAll.assert_called_once()
        repo.findAll.assert_called_with()
        assert tags == self._tags_list
