from dataclasses import dataclass, field

from src_users.domain.common import Entity
from src_users.domain.user.exceptions import AvatarIsDeleted
from src_users.domain.user.value_objects import AvatarId, AvatarType, AvatarUserId


@dataclass
class AvatarEntity(Entity):
    """
    Информация о файле
    """

    avatar_id: AvatarId
    avatar_type: AvatarType
    avatar_user_id: AvatarUserId
    deleted: bool = field(default=False)

    @classmethod
    def create_avatar(
        cls,
        *,
        avatar_user_id: AvatarUserId,
        avatar_name: AvatarId,
        avatar_type: AvatarType,
    ) -> "AvatarEntity":
        """
        Создание файла
        """
        avatar = AvatarEntity(
            avatar_user_id=avatar_user_id,
            avatar_id=avatar_name,
            avatar_type=avatar_type,
        )

        return avatar

    def get_full_avatar_name(self) -> str:
        """
        Поулчение имя файла
        """
        return f"{self.avatar_id.to_uuid}.{self.avatar_type.get_value}"

    def delete(self) -> None:
        """
        Удаление аватара
        """
        self.deleted = True

    def _check_on_delete(self) -> None:
        if self.deleted:
            raise AvatarIsDeleted()
