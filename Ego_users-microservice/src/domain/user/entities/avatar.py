from dataclasses import (
    dataclass,
    field
)

from src.domain.user.exceptions import AvatarIsDeleted
from src.domain.common import (
    Empty,
    Entity
)
from src.domain.user.value_objects import (
    AvatarId,
    AvatarType,
    AvatarUserId
)


@dataclass
class AvatarEntity(Entity):
    """
    Информация о файле
    """
    avatar_user_id: AvatarUserId
    avatar_id: AvatarId
    avatar_type: AvatarType
    avatar_content: bytes
    deleted: bool = field(default=False)

    @classmethod
    def create_avatar(
            cls,
            *,
            user_id: AvatarUserId,
            avatar_id: AvatarId,
            avatar_type: AvatarType,
            avatar_content: bytes
    ) -> 'AvatarEntity':
        """
        Создание файла
        """
        avatar = AvatarEntity(
            avatar_user_id=user_id,
            avatar_id=avatar_id,
            avatar_type=avatar_type,
            avatar_content=avatar_content
        )

        return avatar

    def update_avatar(
            self,
            *,
            avatar_type: AvatarType | Empty = Empty.UNSET,
            avatar_content: bytes | Empty = Empty.UNSET
        ) -> None:
        """
        Обнавление фотографии
        """
        self._check_on_delete()

        if avatar_type is not Empty.UNSET:
            self.avatar_type = avatar_type
        if avatar_content is not Empty.UNSET:
            self.avatar_content = avatar_content

    def delete(self) -> None:
        """
        Удаление аватара
        """
        self.deleted = True

    def _check_on_delete(self) -> None:
        if self.deleted:
            raise AvatarIsDeleted()
