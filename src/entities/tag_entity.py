"""Tag Entity"""

import json
import uuid
from dataclasses import dataclass, asdict


@dataclass
class Tag:
    """Tag Entity"""

    id: uuid.UUID
    title: str

    @classmethod
    def from_dict(cls, data: dict):
        """Initializes Tag class from dictionary object"""
        return cls(**data)

    def to_dict(self):
        """Converts Tag class to dictionary object"""
        return asdict(self)

    def to_json(self):
        """Converts Tag class to string"""
        return json.dumps(self, default=lambda o: o.__dict__)
