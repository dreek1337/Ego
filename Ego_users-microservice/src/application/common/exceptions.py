from dataclasses import dataclass

from src.domain.common import AbstractBaseException


class AppException(AbstractBaseException):
    """Ошибка прикладного уровня"""


@dataclass
class UnexpectedError(AbstractBaseException):
    text: str

    def message(self) -> str:
        return self.text


@dataclass
class CommitError(UnexpectedError):
    """Ошибка коммита для бд"""


@dataclass
class RollbackError(UnexpectedError):
    """Ошибка роллбека для бд"""
