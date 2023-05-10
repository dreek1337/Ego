from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class UserId:
    value: int


@dataclass(frozen=True)
class UserName:
    value: str


@dataclass(frozen=True)
class UserEmail:
    value: str


@dataclass(frozen=True)
class UserPassword:
    value: str


@dataclass(frozen=True)
class UserGender:
    value: str


@dataclass(frozen=True)
class UserBirthday:
    value: date


@dataclass(frozen=True)
class UserRegistrationDate:
    value: date


@dataclass(frozen=True)
class UserActive:
    value: bool


@dataclass(frozen=True)
class UserRights:
    value: str
