from abc import (
    ABC,
    abstractmethod
)

from src.domain import AvatarEntity
from src.domain.user.value_objects import UserId


class AvatarRepo(ABC):
    """
    Репозиторий файла
    """
    @abstractmethod
    async def get_avatar_by_id(self, user_id: UserId) -> AvatarEntity:
        """Получение файла с помощью id"""

    @abstractmethod
    async def set_avatar(
            self,
            *,
            user_id: UserId,
            avatar: AvatarEntity
    ) -> None:
        """Сохранение файла"""

    @abstractmethod
    async def update_avatar(self, avatar: AvatarEntity) -> None:
        """Удаление файла"""
