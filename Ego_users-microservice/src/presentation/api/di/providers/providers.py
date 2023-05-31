from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker
)

from src.application.user.service.user_service import UserService
from src.presentation.api.di.providers.stubs import get_mapper_stub, get_uow_stub
from src.infrastructure.mapper.main import MapperImpl
from src.infrastructure.database import repositories as repo
from src.infrastructure.database.uow.uow import SQLAlchemyUoW


class UoWProvider:
    def __init__(
            self,
            *,
            mapper: MapperImpl,
            pool: async_sessionmaker[AsyncSession]
    ) -> None:
        self.pool = pool
        self.mapper = mapper

    async def get_uow(self) -> SQLAlchemyUoW:
        """
        Получение UoW с подключением к бд
        """
        async with self.pool() as session:
            return SQLAlchemyUoW(
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


class ServiceProvider:
    def __init__(
            self,
            *,
            uow: SQLAlchemyUoW = Depends(get_uow_stub),
            mapper: MapperImpl = Depends(get_mapper_stub)
    ) -> None:
        self.uow = uow
        self.mapper = mapper

    def get_service(self) -> UserService:
        """
        Поулчение Пользовательского сервиса со всеми зависимостями
        """
        return UserService(uow=self.uow, mapper=self.mapper)
