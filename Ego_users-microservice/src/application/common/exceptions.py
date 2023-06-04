from dataclasses import (
    field,
    dataclass
)

from src.domain.common import AbstractBaseException


class AppException(AbstractBaseException):
    """Ошибка прикладного уровня"""


@dataclass
class UnexpectedError(AbstractBaseException):
    file_name: str | None = field(default=None)
    content: tuple | None = field(default=None)


@dataclass
class CommitError(UnexpectedError):
    """Ошибка коммита для бд"""


@dataclass
class RollbackError(UnexpectedError):
    """Ошибка роллбека для бд"""


@dataclass
class RepoError(UnexpectedError):
    """Неизвестная ошибка репозитория"""
