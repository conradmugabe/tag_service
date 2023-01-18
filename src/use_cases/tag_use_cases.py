"""Tag Use Cases"""

from abc import ABC, abstractmethod


class TagDatabaseService(ABC):
    """Tag Database Service"""

    @abstractmethod
    def find_all(self):
        """Retrieves tags"""


class TagUseCases:
    """Tag Use Cases"""

    def __init__(self, database_service: TagDatabaseService):
        self.database_service = database_service

    def getAll(self):
        """Retrieves tags from database services"""
        return self.database_service.find_all()
