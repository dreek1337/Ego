from typing import Callable

from src.application import Mapper


class ElasticPostRepoBase:
    """
    Базвоый класс репзитория
    """
    def __init__(
            self,
            *,
            mapper: Mapper,
            engine: Callable
    ) -> None:
        self._engine = engine
        self._mapper = mapper
