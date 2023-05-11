from dataclasses import dataclass


@dataclass(frozen=True)
class UserGender:
    value: str
