from typing import AsyncContextManager, AsyncGenerator, Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from src.application.user.service.user_service import UserService
from src.infrastructure.database import SQLAlchemyUoW, repositories as repo
from src.infrastructure.mapper import MapperImpl
from src.infrastructure.simple_storage_service import UserCloudStorageImpl
from src.presentation.api.di.providers.stubs import (
    get_cloud_storage_stub,
    get_mapper_stub,
    get_uow_stub,
)


class InfrastructureProvider:
    def __init__(
        self,
        *,
        mapper: MapperImpl,
        cloud_connection: Callable[..., AsyncContextManager],
        pool: async_sessionmaker[AsyncSession],
    ) -> None:
        self._pool = pool
        self._mapper = mapper
        self._cloud_connection = cloud_connection

    async def get_uow(self) -> AsyncGenerator[SQLAlchemyUoW, None]:
        """
        Получение UoW с подключением к бд
        """
        async with self._pool() as session:
            uow = SQLAlchemyUoW(
                session=session,
                user_repo=repo.UserRepoImpl(session=session, mapper=self._mapper),
                avatar_repo=repo.AvatarRepoImpl(session=session, mapper=self._mapper),
                subscription_repo=repo.SubscriptionRepoImpl(
                    session=session, mapper=self._mapper
                ),
                subscription_reader=repo.SubscriptionReaderImpl(
                    session=session, mapper=self._mapper
                ),
            )

            yield uow

    def get_cloud_storage(self) -> UserCloudStorageImpl:
        """
        Получение асинхронное подключение к minio
        """
        cloud_storage = UserCloudStorageImpl(connection=self._cloud_connection)

        return cloud_storage


def get_service(
    uow: SQLAlchemyUoW = Depends(get_uow_stub),
    mapper: MapperImpl = Depends(get_mapper_stub),
    cloud_storage: UserCloudStorageImpl = Depends(get_cloud_storage_stub),
) -> UserService:
    """
    Поулчение Пользовательского сервиса со всеми зависимостями
    """
    return UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage)
