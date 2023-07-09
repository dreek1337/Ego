from dataclasses import dataclass

from src_users.domain.common import ValueObject


@dataclass(frozen=True)
class SubscriptionId(ValueObject[int]):
    value: int

    @property
    def to_int(self) -> int:
        return self.value
