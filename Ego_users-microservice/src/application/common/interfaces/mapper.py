from abc import (
    ABC,
    abstractmethod
)
from typing import Any, TypeVar

T = TypeVar("T")


class Mapper(ABC):
    @abstractmethod
    def load(self, data: Any, model: type[T]) -> T:
        """Переработка данных в другую модель"""
