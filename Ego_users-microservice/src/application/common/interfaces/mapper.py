from abc import (
    ABC,
    abstractmethod
)
from typing import Any, TypeVar

T = TypeVar("T")


class Mapper(ABC):
    @abstractmethod
    def load(self, data: Any, class_: type[T]) -> T:
        """Переработка модели в другую модель"""
