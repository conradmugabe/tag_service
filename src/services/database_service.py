"""Database Service"""

from abc import ABC, abstractmethod


class TagDatabaseService(ABC):
    """Tag Database Service"""

    @abstractmethod
    def find_all(self):
        """Retrieves tags"""
