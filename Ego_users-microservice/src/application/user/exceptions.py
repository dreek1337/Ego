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
