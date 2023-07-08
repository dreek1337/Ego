from abc import (
    ABC,
    abstractmethod,
)

from src_users.application.common import CloudStorageBase
from src_users.application.user.use_cases.avatar.set_avatar import SetAvatarData
from src_users.domain import AvatarEntity


class UserCloudStorage(CloudStorageBase, ABC):
    @abstractmethod
    async def put(self, avatar: SetAvatarData) -> None:
        """Сохранение объекта"""

    @abstractmethod
    async def delete(self, avatar: AvatarEntity) -> None:
        """Удаление объекта"""
