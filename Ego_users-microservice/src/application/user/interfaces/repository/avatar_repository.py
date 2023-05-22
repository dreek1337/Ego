from abc import (
    ABC,
    abstractmethod
)
from typing import Any

from src.domain import AvatarEntity
from src.domain.user.value_objects import AvatarId


class AvatarRepo(ABC):
    """
    Репозиторий файла
    """
    @abstractmethod
    async def get_avatar_by_id(self, avatar_id: AvatarId) -> AvatarEntity:
        """Получение файла с помощью id"""

    @abstractmethod
    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """Сохранение файла"""

    @abstractmethod
    async def delete_avatar(self, avatar_id: AvatarId) -> Any:
        """Удаление файла"""
