from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class AvatarId:
    value: UUID

    @property
    def to_uuid(self) -> UUID:
        return self.value
