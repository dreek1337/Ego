from dataclasses import dataclass
from abc import (
    ABC,
    abstractmethod
)


@dataclass
class BaseAppException(Exception, ABC):
    @abstractmethod
    def message(self) -> str:
        """Сообщение об ошибке"""
