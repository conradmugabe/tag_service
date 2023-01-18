"""In Memory Repository"""

from src.entities.tag_entity import Tag
from src.services.database_service import TagDatabaseService


class InMemoryRepository(TagDatabaseService):
    """In Memory Repository"""

    def __init__(self, tags=[]):
        self.tags = tags

    def find_all(self):
        """Retrieve"""
        return [Tag.from_dict(tag) for tag in self.tags]
