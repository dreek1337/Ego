from dataclasses import dataclass

from src.domain.common import ValueObject


@dataclass(frozen=True)
class AvatarUserId(ValueObject[int]):
    value: int

    @property
    def to_int(self) -> int:
        return self.value
