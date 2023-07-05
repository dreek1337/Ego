from abc import ABC, abstractmethod

from src.application import CloudStorageBase, SetAvatarData
from src.domain import AvatarEntity


class UserCloudStorage(CloudStorageBase, ABC):
    @abstractmethod
    async def put(self, avatar: SetAvatarData) -> None:
        """Сохранение объекта"""

    @abstractmethod
    async def delete(self, avatar: AvatarEntity) -> None:
        """Удаление объекта"""
