from abc import (
    ABC,
    abstractmethod
)

from src.domain import AvatarEntity
from src.domain.user.value_objects import (
    AvatarName,
    AvatarUserId
)


class AvatarRepo(ABC):
    """
    Репозиторий файла
    """
    @abstractmethod
    async def get_avatar_by_user_id(
            self,
            avatar_user_id: AvatarUserId
    ) -> AvatarEntity | None:
        """Получение файла с помощью id"""

    @abstractmethod
    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """Сохранение файла"""

    @abstractmethod
    async def delete_avatar(self, avatar_id: AvatarName | None) -> None:
        """Удаление файла"""
