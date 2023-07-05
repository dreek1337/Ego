from uuid import UUID

from src_users.application import AvatarRepo
from src_users.domain import AvatarEntity
from src_users.domain.user.value_objects import AvatarId, AvatarUserId


class AvatarRepoMock(AvatarRepo):
    """
    Репозиторий файла
    """

    def __init__(self) -> None:
        self.avatars: dict[UUID, AvatarEntity] = dict()

    async def get_avatar_by_user_id(
        self, avatar_user_id: AvatarUserId
    ) -> AvatarEntity | None:
        """
        Получение файла с помощью id
        """
        for avatar in self.avatars.values():
            if avatar.avatar_user_id == avatar_user_id:
                return avatar
        return None

    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """
        Сохранение файла
        """
        self.avatars[avatar.avatar_id.value] = avatar

    async def delete_avatar(self, avatar_id: AvatarId) -> None:
        """
        Удаление файла
        """
        del self.avatars[avatar_id.to_uuid]
