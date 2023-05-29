from src.domain import UserAggregate
from src.application import (
    UserDTO,
    AvatarDTO
)


def convert_user_aggregate_to_dto(user: UserAggregate) -> UserDTO:
    """
    Преобразование из Агрегата в ДТО
    """
    user_dto = UserDTO(
        user_id=user.user_id.to_int,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender.get_value,
        birthday=user.birthday.get_value,
        avatar=AvatarDTO(
            avatar_id=user.avatar.avatar_id.to_uuid,
            avatar_type=user.avatar.avatar_type.get_value,
            avatar_content=user.avatar.avatar_content,
            user_id=user.avatar.user_id
        ) if user.avatar else None,
        count_of_subscriptions=user.count_of_subscriptions,
        count_of_subscribers=user.count_of_subscribers,
        deleted=user.deleted
    )

    return user_dto
