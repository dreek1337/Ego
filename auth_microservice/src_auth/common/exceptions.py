from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from fastapi_jwt_auth.exceptions import AuthJWTException  # type: ignore


@dataclass
class BaseAppException(Exception, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        """Сообщение об ошибке"""


@dataclass
class BaseJWTException(AuthJWTException):
    """Базовая ошибка jwt"""

    status_code: int
    message: str
