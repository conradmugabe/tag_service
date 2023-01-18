"""Test In Memory Repository"""

import pytest

from src.services.in_memory_repository import InMemoryRepository


@pytest.fixture()
def tags_list():
    """Tags list"""
    return []


class TestInMemoryRepository:
    """Test In Memory Repository"""

    def test_repository_list_without_parameters(self, tags_list):
        """Test find_all returns all tags in the repository"""
        repo = InMemoryRepository(tags=tags_list)

        assert repo.find_all() == tags_list
