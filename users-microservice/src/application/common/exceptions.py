from dataclasses import dataclass

from src.domain.common import AbstractBaseException


class AppException(AbstractBaseException):
    """Ошибка прикладного уровня"""


@dataclass
class UnexpectedError(AbstractBaseException):
    """Базовая ошибка для работы с бд"""


@dataclass
class CommitError(UnexpectedError):
    """Ошибка коммита для бд"""


@dataclass
class RollbackError(UnexpectedError):
    """Ошибка роллбека для бд"""


@dataclass
class RepoError(UnexpectedError):
    """Неизвестная ошибка репозитория"""
