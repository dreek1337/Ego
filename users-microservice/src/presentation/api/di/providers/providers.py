from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker
)

from src.infrastructure.mapper import MapperImpl
from src.infrastructure.database import SQLAlchemyUoW
from src.infrastructure.database import repositories as repo
from src.application.user.service.user_service import UserService
from src.infrastructure.simple_storage_service import (
    MinioConfig,
    CloudStorageImpl
)
from src.presentation.api.di.providers.stubs import (
    get_uow_stub,
    get_mapper_stub,
    get_cloud_storage_stub
)


class InfrastructureProvider:
    def __init__(
            self,
            *,
            mapper: MapperImpl,
            cloud_config: MinioConfig,
            pool: async_sessionmaker[AsyncSession]
    ) -> None:
        self._pool = pool
        self._mapper = mapper
        self._cloud_config = cloud_config

    async def get_uow(self) -> AsyncGenerator[SQLAlchemyUoW, None]:
        """
        Получение UoW с подключением к бд
        """
        async with self._pool() as session:
            uow = SQLAlchemyUoW(
                session=session,
                user_repo=repo.UserRepoImpl(
                    session=session,
                    mapper=self._mapper
                ),
                avatar_repo=repo.AvatarRepoImpl(
                    session=session,
                    mapper=self._mapper
                ),
                subscription_repo=repo.SubscriptionRepoImpl(
                    session=session,
                    mapper=self._mapper
                ),
                subscription_reader=repo.SubscriptionReaderImpl(
                    session=session,
                    mapper=self._mapper
                )
            )

            yield uow

    def get_cloud_storage(self) -> CloudStorageImpl:
        """
        Получение асинхронное подключение к minio
        """
        cloud_storage = CloudStorageImpl(
            cloud_config=self._cloud_config
        )

        return cloud_storage


def get_service(
        uow: SQLAlchemyUoW = Depends(get_uow_stub),
        mapper: MapperImpl = Depends(get_mapper_stub),
        cloud_storage: CloudStorageImpl = Depends(get_cloud_storage_stub)
) -> UserService:
    """
    Поулчение Пользовательского сервиса со всеми зависимостями
    """
    return UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage)
