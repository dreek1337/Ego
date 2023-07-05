from src_users.application import DeletedUserDTO, UserDTO
from src_users.domain import UserAggregate
from src_users.domain.common import GenderValue
from src_users.domain.user import value_objects as vo
from src_users.infrastructure.database.models import Users


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
        avatar_path=user.avatar_path if user.avatar_path else None,
        count_of_subscriptions=user.count_of_subscriptions,
        count_of_subscribers=user.count_of_subscribers,
        deleted=user.deleted,
    )

    return user_dto


def convert_deleted_user_aggregate_to_dto(user: UserAggregate) -> DeletedUserDTO:
    """
    Преобразование из Агрегата в ДТО
    """
    deleted_user_dto = DeletedUserDTO(
        user_id=user.user_id.to_int,
        first_name=user.first_name,
        last_name=user.last_name,
        deleted=user.deleted,
    )

    return deleted_user_dto


def convert_user_aggregate_to_db_model(user: UserAggregate) -> Users:
    """
    Преобразование из Агрегата в ORM модель
    """
    orm_model = Users(
        user_id=user.user_id.to_int,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender.get_value,
        birthday=user.birthday.get_value,
        deleted=user.deleted,
    )

    return orm_model


def convert_db_model_to_user_aggregate(user: Users) -> UserAggregate:
    """
    Преобразование из ORM модели в Агрегат
    """
    user_aggregate = UserAggregate(
        user_id=vo.UserId(value=user.user_id),
        first_name=user.first_name,
        last_name=user.last_name,
        gender=vo.UserGender(
            value=GenderValue.MALE if user.gender == "male" else GenderValue.FEMALE
        ),
        birthday=vo.UserBirthday(value=user.birthday),
        deleted=user.deleted,
    )

    return user_aggregate


def convert_db_model_to_user_dto(user: Users) -> UserDTO:
    """
    Преобразование из модели орм в ДТО
    """
    user_dto = UserDTO.from_orm(user)

    return user_dto


def convert_db_model_to_deleted_user_dto(user: Users) -> DeletedUserDTO:
    """
    Преобразование из модели орм в ДТО
    """
    deleted_user_dto = DeletedUserDTO.from_orm(user)

    return deleted_user_dto
