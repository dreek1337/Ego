from uuid import UUID
from dataclasses import dataclass

from src.application.common.exceptions import AppException


@dataclass
class UserIsNotExist(AppException):
    user_id: int

    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'A user with the "{self.user_id}" user_id is not exists'


@dataclass
class UserIdIsAlreadyExist(AppException):
    user_id: int

    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'A user with the "{self.user_id}" user_id already exists'


@dataclass
class AvatarIdIsAlreadyExist(AppException):
    avatar_id: UUID

    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'Avatar with the "{self.avatar_id}" avatar_id already exists'


@dataclass
class AvatarIsNotExist(AppException):
    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Avatar is not exists'


@dataclass
class UnsupportedConvertor(AppException):
    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'ToModel or FromModel is unsupported!'


@dataclass
class SubscribeOnYourself(AppException):
    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'You can\'t subscribe on yourself!'


@dataclass
class SubscribeIsAlreadyExists(AppException):
    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Subscribe is already exists!'


@dataclass
class SubscribeIsNotExists(AppException):
    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Subscribe is not exists!'
