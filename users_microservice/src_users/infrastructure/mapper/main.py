from typing import (
    Any,
    TypeVar,
)

from sqlalchemy import ChunkedIteratorResult
from src_users import (
    application as app,
    domain,
)
from src_users.application import UnsupportedConvertor
from src_users.infrastructure.database import models
from src_users.infrastructure.mapper import convert_functions as cf
from src_users.infrastructure.mapper.convert import Convert

FromModel = TypeVar("FromModel", bound=Any)
ToModel = TypeVar("ToModel", bound=Any)


class MapperImpl(app.Mapper):
    """
    Реализация маппера
    """

    def __init__(self, convert_mappers: list[Convert]) -> None:
        self._convert_mappers = convert_mappers

    def load(self, *, from_model: FromModel, to_model: type[ToModel]) -> ToModel:
        """
        Преобразование из одной модели в другую
        """
        convert = self._get_convert(from_model=from_model, to_model=to_model)

        return convert.load(from_model=from_model)

    def _get_convert(
        self, *, from_model: FromModel, to_model: type[ToModel]
    ) -> Convert:
        """
        Получение нужного Convert
        """
        for convert in self._convert_mappers:
            if convert.check(from_model=type(from_model), to_model=to_model):
                return convert
        raise UnsupportedConvertor()


def create_mapper() -> MapperImpl:
    """
    Инициализация маппера
    """
    mapper = MapperImpl(
        convert_mappers=(
            [
                Convert(
                    from_model=domain.UserAggregate,
                    to_model=app.UserDTO,
                    loader=cf.convert_user_aggregate_to_dto,
                ),
                Convert(
                    from_model=domain.UserAggregate,
                    to_model=app.DeletedUserDTO,
                    loader=cf.convert_deleted_user_aggregate_to_dto,
                ),
                Convert(
                    from_model=domain.UserAggregate,
                    to_model=models.Users,
                    loader=cf.convert_user_aggregate_to_db_model,
                ),
                Convert(
                    from_model=models.Users,
                    to_model=domain.UserAggregate,
                    loader=cf.convert_db_model_to_user_aggregate,
                ),
                Convert(
                    from_model=models.Users,
                    to_model=app.UserDTO,
                    loader=cf.convert_db_model_to_user_dto,
                ),
                Convert(
                    from_model=models.Users,
                    to_model=app.DeletedUserDTO,
                    loader=cf.convert_db_model_to_deleted_user_dto,
                ),
                Convert(
                    from_model=domain.AvatarEntity,
                    to_model=app.AvatarDTO,
                    loader=cf.convert_avatar_entity_to_dto,
                ),
                Convert(
                    from_model=domain.AvatarEntity,
                    to_model=app.DeletedAvatarDTO,
                    loader=cf.convert_deleted_avatar_entity_to_dto,
                ),
                Convert(
                    from_model=domain.AvatarEntity,
                    to_model=models.Avatars,
                    loader=cf.convert_avatar_entity_to_db_model,
                ),
                Convert(
                    from_model=models.Avatars,
                    to_model=domain.AvatarEntity,
                    loader=cf.convert_db_model_to_avatar_entity,
                ),
                Convert(
                    from_model=models.Avatars,
                    to_model=app.AvatarDTO,
                    loader=cf.convert_db_model_to_avatar_dto,
                ),
                Convert(
                    from_model=models.Avatars,
                    to_model=app.DeletedAvatarDTO,
                    loader=cf.convert_db_model_to_deleted_avatar_dto,
                ),
                Convert(
                    from_model=domain.SubscriptionEntity,
                    to_model=app.SubscribeActionDTO,
                    loader=cf.convert_subscription_entity_to_dto,
                ),
                Convert(
                    from_model=ChunkedIteratorResult,
                    to_model=list[app.SubscriptionDTO],
                    loader=cf.convert_subscriptions_db_model_to_subscription_dto,
                ),
                Convert(
                    from_model=models.Subscriptions,
                    to_model=domain.SubscriptionEntity,
                    loader=cf.convert_subscription_db_model_to_subscription_entity,
                ),
                Convert(
                    from_model=domain.SubscriptionEntity,
                    to_model=models.Subscriptions,
                    loader=cf.convert_subscription_entity_to_db_model,
                ),
            ]
        )
    )

    return mapper
