from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker
)

from src.infrastructure.mapper.main import MapperImpl
from src.infrastructure.database import repositories as repo
from src.infrastructure.database.uow.uow import SQLAlchemyUoW
from src.application.user.service.user_service import UserService
from src.presentation.api.di.providers.stubs import (
    get_mapper_stub,
    get_uow_stub
)


class UoWProvider:
    def __init__(
            self,
            *,
            mapper: MapperImpl,
            pool: async_sessionmaker[AsyncSession]
    ) -> None:
        self.pool = pool
        self.mapper = mapper

    async def get_uow(self) -> AsyncGenerator[SQLAlchemyUoW, None]:
        """
        Получение UoW с подключением к бд
        """
        async with self.pool() as session:
            uow = SQLAlchemyUoW(
                session=session,
                user_repo=repo.UserRepoImpl(
                    session=session,
                    mapper=self.mapper
                ),
                avatar_repo=repo.AvatarRepoImpl(
                    session=session,
                    mapper=self.mapper
                ),
                subscription_repo=repo.SubscriptionRepoImpl(
                    session=session,
                    mapper=self.mapper
                ),
                subscription_reader=repo.SubscriptionReaderImpl(
                    session=session,
                    mapper=self.mapper
                )
            )

            yield uow


def get_service(
        uow: SQLAlchemyUoW = Depends(get_uow_stub),
        mapper: MapperImpl = Depends(get_mapper_stub)
) -> UserService:
    """
    Поулчение Пользовательского сервиса со всеми зависимостями
    """
    return UserService(uow=uow, mapper=mapper)  # type: ignore
