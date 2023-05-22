from dataclasses import dataclass


@dataclass(frozen=True)
class SubscriptionId:
    value: int

    @property
    def to_int(self) -> int:
        return self.value
