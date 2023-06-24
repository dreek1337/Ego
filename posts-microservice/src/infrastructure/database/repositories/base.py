from elasticsearch import AsyncElasticsearch  # type: ignore

from src.application import Mapper


class PostRepoBase:
    """
    Базвоый класс репзитория
    """
    def __init__(
            self,
            *,
            mapper: Mapper,
            connection: AsyncElasticsearch
    ) -> None:
        self._connection = connection
        self._mapper = mapper
