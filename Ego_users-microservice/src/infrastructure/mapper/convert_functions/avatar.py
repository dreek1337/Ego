from src.domain import AvatarEntity
from src.domain.user import value_objects as vo
from src.infrastructure.database.models import Avatars
from src.application import (
    AvatarDTO,
    DeletedAvatarDTO,
)


def convert_avatar_entity_to_dto(avatar: AvatarEntity) -> AvatarDTO:
    """
    Преобразование Энтити в ДТО
    """
    avatar_dto = AvatarDTO(
        avatar_name=avatar.avatar_name.to_uuid,
        avatar_type=avatar.avatar_type.get_value,
        avatar_user_id=avatar.avatar_user_id.to_int
    )

    return avatar_dto


def convert_deleted_avatar_entity_to_dto(avatar: AvatarEntity) -> DeletedAvatarDTO:
    """
    Преобразование удаленный Энтити в ДТО
    """
    avatar_deleted_dto = DeletedAvatarDTO(
        avatar_id=avatar.avatar_name.to_uuid
    )

    return avatar_deleted_dto


def convert_avatar_entity_to_db_model(avatar: AvatarEntity) -> Avatars:
    """
    Преобразование Энтити в ORM модель
    """
    avatar_model = Avatars(
        avatar_id=avatar.avatar_name.to_uuid,
        avatar_type=avatar.avatar_type.get_value,
        avatar_user_id=avatar.avatar_user_id.to_int
    )

    return avatar_model


def convert_db_model_to_avatar_entity(avatar: Avatars) -> AvatarEntity:
    """
    Преобразование ORM модели в Энтити
    """
    avatar_entity = AvatarEntity(
        avatar_name=vo.AvatarName(
            value=avatar.avatar_id
        ),
        avatar_type=vo.AvatarType(
            value=avatar.avatar_type
        ),
        avatar_user_id=vo.AvatarUserId(
            value=avatar.avatar_user_id
        )
    )

    return avatar_entity


def convert_db_model_to_avatar_dto(avatar: Avatars) -> AvatarDTO:
    """
    Преобразование из модели орм в ДТО
    """
    avatar_dto = AvatarDTO.from_orm(avatar)

    return avatar_dto


def convert_db_model_to_deleted_avatar_dto(avatar: Avatars) -> DeletedAvatarDTO:
    """
    Преобразование из модели орм в ДТО
    """
    print()
    deleted_avatar_dto = DeletedAvatarDTO.from_orm(avatar)

    return deleted_avatar_dto
