from abc import ABC, abstractmethod
from typing import Any, TypeVar

FromModel = TypeVar("FromModel", bound=Any)
ToModel = TypeVar("ToModel", bound=Any)


class Mapper(ABC):
    @abstractmethod
    def load(self, *, from_model: FromModel, to_model: type[ToModel]) -> ToModel:
        """Переработка данных в другую модель"""
