from datetime import date
from dataclasses import dataclass


@dataclass(frozen=True)
class PostId:
    value: int


@dataclass(frozen=True)
class PostText:
    value: str


@dataclass(frozen=True)
class PostLike:
    value: int


@dataclass(frozen=True)
class DateOfCreate:
    value: date