"""Tag Command Line Interface"""

from src.use_cases.tag_use_cases import TagUseCases
from src.services.in_memory_repository import InMemoryRepository

database_service = InMemoryRepository(tags=[])
tag_use_cases = TagUseCases(database_service=database_service)

print(tag_use_cases.get_all())
