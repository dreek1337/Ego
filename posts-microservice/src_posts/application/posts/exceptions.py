from dataclasses import dataclass

from src_posts.application.common.exceptions import AppException


@dataclass
class UnsupportedConvertor(AppException):
    """
    Нет подходящего Convertor
    """

    @property
    def message(self) -> str:
        """
        Сообщение об ошибке
        """
        return "ToModel or FromModel is unsupported!"


@dataclass
class UserIsNotPostCreator(AppException):
    """
    Нет подходящего Convertor
    """

    @property
    def message(self) -> str:
        """
        Сообщение об ошибке
        """
        return "User is not post creator!"
