from typing import Callable

from elasticsearch import AsyncElasticsearch  # type: ignore

from src.infrastructure.database.config import ElasticEngine


def elastic_factory(config: ElasticEngine) -> Callable:
    """
    Поулчение асинхронного подключения к ЕС
    """
    def create_engine() -> AsyncElasticsearch:
        return AsyncElasticsearch(**config.dict())

    return create_engine
