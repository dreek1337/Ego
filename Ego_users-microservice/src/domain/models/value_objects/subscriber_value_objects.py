from dataclasses import dataclass


@dataclass(frozen=True)
class SubscriberId:
    value: int


@dataclass(frozen=True)
class SubscriberName:
    value: str
