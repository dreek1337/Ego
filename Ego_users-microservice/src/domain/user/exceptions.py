from dataclasses import dataclass
from datetime import date

from src.domain.common import AbstractBaseException


@dataclass
class UserIsDeleted(AbstractBaseException):
    """Ошибка об том, что пользователь удален"""
    user_id: int

    @property
    def message(self) -> str:
        return f'The user with "{self.user_id}" id is deleted'


class AvatarIsDeleted(AbstractBaseException):
    """Ошибка об том, что аватар удален"""
    @property
    def message(self) -> str:
        return 'User hasn\'t avatar'


@dataclass
class InvalidAvatarType(AbstractBaseException):
    file_type: str

    @property
    def message(self) -> str:
        return f'Unsupported file type {self.file_type}'


@dataclass
class InvalidGender(AbstractBaseException):
    gender_type: str

    @property
    def message(self) -> str:
        return f'Unsupported gender type {self.gender_type}'


@dataclass
class InvalidBirthdayDate(AbstractBaseException):
    birthday_date: date

    @property
    def message(self) -> str:
        return f'You can\'t give birth in the future {self.birthday_date}'
