from typing import Callable

from fastapi import Depends

from src.application import PostService
from src.presentation.api.di.providers.stubs import (
    get_uow_stub,
    get_mapper_stub
)
from src.infrastructure import (
    MapperImpl,
    PostRepoImpl,
    PostReaderImpl,
    ElasticsearchUoW
)


class InfrastructureProvider:
    def __init__(
            self,
            *,
            mapper: MapperImpl,
            engine: Callable
    ) -> None:
        self._mapper = mapper
        self._engine = engine

    def get_uow(self) -> ElasticsearchUoW:
        uow = ElasticsearchUoW(
            post_repo=PostRepoImpl(
                mapper=self._mapper,
                engine=self._engine
            ),
            post_reader=PostReaderImpl(
                mapper=self._mapper,
                engine=self._engine
            )
        )

        return uow


def get_service(
        uow: ElasticsearchUoW = Depends(get_uow_stub),
        mapper: MapperImpl = Depends(get_mapper_stub),
) -> PostService:
    """
    Поулчение сервиса со всеми зависимостями
    """
    return PostService(uow=uow, mapper=mapper)
