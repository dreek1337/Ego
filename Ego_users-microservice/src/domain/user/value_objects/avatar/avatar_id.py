from dataclasses import dataclass
from uuid import UUID

from src.domain.common import ValueObject


@dataclass(frozen=True)
class AvatarId(ValueObject[UUID]):
    value: UUID

    @property
    def to_uuid(self) -> UUID:
        return self.value
