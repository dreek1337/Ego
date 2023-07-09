from typing import Callable

from fastapi import Depends
from src_posts.application import PostService
from src_posts.infrastructure import (
    ElasticsearchUoW,
    MapperImpl,
    PostReaderImpl,
    PostRepoImpl,
)
from src_posts.presentation.api.di.providers.stubs import (
    get_mapper_stub,
    get_uow_stub,
)


class InfrastructureProvider:
    def __init__(self, *, mapper: MapperImpl, engine: Callable) -> None:
        self._mapper = mapper
        self._engine = engine

    def get_uow(self) -> ElasticsearchUoW:
        uow = ElasticsearchUoW(
            post_repo=PostRepoImpl(mapper=self._mapper, engine=self._engine),
            post_reader=PostReaderImpl(mapper=self._mapper, engine=self._engine),
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
