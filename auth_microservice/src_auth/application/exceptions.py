from dataclasses import dataclass

from src_auth.common import BaseAppException


@dataclass
class UserDataIsNotCorrect(BaseAppException):
    """Ошибка о том, что введенные данные были некорректны"""

    @property
    def message(self) -> str:
        return "Username or password is not correct!"


@dataclass
class UserIsNotExists(BaseAppException):
    """Ошибка о том, что айди отсутвует в базе"""

    user_id: int

    @property
    def message(self) -> str:
        return f"User with {self.user_id} is not exists!"


@dataclass
class CommitError(BaseAppException):
    """Ошибка коммита для бд"""

    @property
    def message(self) -> str:
        return "Somthing wrong with commit!"


@dataclass
class RollbackError(BaseAppException):
    """Ошибка роллбека для бд"""

    @property
    def message(self) -> str:
        return "Somthing wrong with rollback!"


@dataclass
class RepoError(BaseAppException):
    """Неизвестная ошибка репозитория"""

    @property
    def message(self) -> str:
        return "Somthing wrong in repository!"


@dataclass
class UsernameIsAlreadyExist(BaseAppException):
    """Ошибка о том, что имя пользователя уже занято"""

    username: str

    @property
    def message(self) -> str:
        return f"User with {self.username} is already exists!"
