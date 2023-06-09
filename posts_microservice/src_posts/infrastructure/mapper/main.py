from typing import (
    Any,
    TypeVar,
)

from src_posts import (
    application as app,
    domain,
)
from src_posts.application import UnsupportedConvertor
from src_posts.application.posts import dto
from src_posts.infrastructure.mapper import convert_functions as cf
from src_posts.infrastructure.mapper.convert import Convert

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
        print()
        raise UnsupportedConvertor()


def create_mapper() -> MapperImpl:
    """
    Инициализация маппера
    """
    mapper = MapperImpl(
        convert_mappers=(
            [
                Convert(
                    from_model=domain.PostAggregate,
                    to_model=dto.PostDTO,
                    loader=cf.convert_from_entity_to_dto,
                ),
                Convert(
                    from_model=dict,
                    to_model=domain.PostAggregate,
                    loader=cf.convert_from_elastic_model_to_entity,
                ),
                Convert(
                    from_model=list,
                    to_model=list[dto.PostDTO],
                    loader=cf.convert_from_elastic_models_to_dto,
                ),
            ]
        )
    )

    return mapper
