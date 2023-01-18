import uuid
from dataclasses import dataclass, asdict


@dataclass
class Tag:
    id: uuid.UUID
    title: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_dict(self):
        return asdict(self)
