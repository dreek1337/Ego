from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    TypeVar,
)

SaveData = TypeVar("SaveData", bound=Any)
DeleteData = TypeVar("DeleteData", bound=Any)


class CloudStorageBase(ABC):
    """
    Базовый класс с3 сервиса
    """

    @abstractmethod
    async def put(self, avatar: SaveData) -> None:
        """Сохранение объекта"""

    @abstractmethod
    async def delete(self, avatar: DeleteData) -> None:
        """Удаление объекта"""
