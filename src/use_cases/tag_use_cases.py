"""Tag Use Cases"""

from src.services.database_service import TagDatabaseService


class TagUseCases:
    """Tag Use Cases"""

    def __init__(self, database_service: TagDatabaseService):
        self.database_service = database_service

    def get_all(self):
        """Retrieves tags from database services"""
        return self.database_service.find_all()
