from typing import (
    Any,
    TypeVar
)

from src import application as app
from src.application import UnsupportedConvertor
from src.infrastructure.mapper.convert import Convert

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
        raise UnsupportedConvertor()


def create_mapper() -> MapperImpl:
    """
    Инициализация маппера
    """
    mapper = MapperImpl(convert_mappers=(
            ...  # type: ignore
        )
    )

    return mapper
