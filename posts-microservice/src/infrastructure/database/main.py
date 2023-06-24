from elasticsearch import AsyncElasticsearch  # type: ignore

from src.infrastructure.database.config import ElasticEngine


def elastic_factory(config: ElasticEngine) -> AsyncElasticsearch:
    """
    Поулчение асинхронного подключения к ЕС
    """
    es = AsyncElasticsearch(**config.dict())

    return es
