from typing import (
    Any,
    TypeVar
)

from src import application as app
from src.domain import UserAggregate
from src.infrastructure.database import models
from src.infrastructure.mapper.convert import Convert
from src.infrastructure.mapper import convert_functions as cf

FromModel = TypeVar("FromModel", bound=Any)
ToModel = TypeVar("ToModel", bound=Any)


class MapperImpl(app.Mapper):
    """
    Реализация маппера
    """
    def __init__(self, convert_mappers: list[Convert]) -> None:
        self._convert_mappers = convert_mappers

    def load(
            self,
            *,
            from_model: FromModel,
            to_model: type[ToModel]
    ) -> ToModel:
        """
        Преобразование из одной модели в другую
        """
        convert = self._get_convert(from_model=from_model, to_model=to_model)

        return convert.load(from_model=from_model)

    def _get_convert(
            self,
            *,
            from_model: FromModel,
            to_model: type[ToModel]
    ) -> Convert:
        """
        Получение нужного Convert
        """
        for convert in self._convert_mappers:
            if convert.check(from_model=type(from_model), to_model=to_model):
                return convert
        # Сделать ошибку, что подходящего Convert нет
        raise Exception


def create_convert() -> MapperImpl:
    """
    Инициализация маппера
    """
    mapper = MapperImpl(convert_mappers=([
        Convert(
            from_model=UserAggregate,
            to_model=app.UserDTO,
            loader=cf.convert_user_aggregate_to_dto
        ),
        Convert(
            from_model=UserAggregate,
            to_model=app.DeletedUserDTO,
            loader=cf.convert_deleted_user_aggregate_to_dto
        ),
        Convert(
            from_model=UserAggregate,
            to_model=models.Users,
            loader=cf.convert_user_aggregate_to_db_model
        ),
        Convert(
            from_model=models.Users,
            to_model=UserAggregate,
            loader=cf.convert_db_model_to_user_aggregate
        ),
        Convert(
            from_model=models.Users,
            to_model=app.UserDTO,
            loader=cf.convert_db_model_to_user_dto
        ),
        Convert(
            from_model=models.Users,
            to_model=app.DeletedUserDTO,
            loader=cf.convert_db_model_to_deleted_user_dto
        )
    ]))

    return mapper
