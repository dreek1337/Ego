from dataclasses import dataclass


@dataclass(frozen=True)
class SubscriptionId:
    value: int


@dataclass(frozen=True)
class SubscriptionName:
    value: str
