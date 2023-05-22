from dataclasses import dataclass


@dataclass(frozen=True)
class AvatarType:
    value: str
