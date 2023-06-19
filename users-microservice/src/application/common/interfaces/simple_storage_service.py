from typing import (
    Any,
    TypeVar
)
from abc import (
    ABC,
    abstractmethod
)

SaveData = TypeVar('SaveData', bound=Any)
DeleteData = TypeVar('DeleteData', bound=Any)


class CloudStorageBase(ABC):
    """
    Базовый класс с3 сервиса
    """
    @abstractmethod
    async def put(self, data: SaveData) -> None:
        """Сохранение объекта"""

    @abstractmethod
    async def delete(self, data: DeleteData) -> None:
        """Удаление объекта"""
