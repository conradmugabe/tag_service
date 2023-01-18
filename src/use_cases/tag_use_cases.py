from abc import ABC, abstractmethod


class TagDatabaseService(ABC):
    @abstractmethod
    def findAll(self):
        pass


class TagUseCases:
    def __init__(self, database_service: TagDatabaseService):
        self.database_service = database_service

    def getAll(self):
        return self.database_service.findAll()
