from typing import Self

from dataclasses import dataclass

from src.domain.user.value_objects import (
    AvatarType,
    AvatarId
)


@dataclass
class AvatarEntity:
    """
    Информация о файле
    """
    avatar_id: AvatarId
    avatar_type: AvatarType
    avatar_content: bytes

    @classmethod
    def set_avatar(
            cls,
            *,
            avatar_id: AvatarId,
            avatar_type: AvatarType,
            avatar_content: bytes
    ) -> Self:
        """
        Создание файла
        """
        avatar = AvatarEntity(
            avatar_id=avatar_id,
            avatar_type=avatar_type,
            avatar_content=avatar_content
        )

        return avatar
