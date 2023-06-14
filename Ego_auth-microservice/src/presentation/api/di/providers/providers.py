from typing import AsyncGenerator

from fastapi import Depends
from passlib.context import CryptContext  # type: ignore
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker
)

from src.application import AuthService
from src.infra.database.uow.uow import SQLAlchemyUoW
from src.infra import (
    UserRepositoryImpl,
    PasswordManagerImpl,
    AccessTokenManagerImpl
)
from src.presentation.api.di.providers.stubs import (
    get_uow_stub,
    get_token_manager_stub,
    get_password_manager_stub
)


class InfraProvider:
    """
    Класс для инициализации логики из инфарструктуры
    """
    def __init__(
            self,
            *,
            pwd_context: CryptContext,
            pool: async_sessionmaker[AsyncSession]
    ) -> None:
        self._pool = pool
        self._pwd_context = pwd_context

    async def get_uow(self) -> AsyncGenerator[SQLAlchemyUoW, None]:
        """
        Инициализация uow
        """
        async with self._pool() as session:
            uow = SQLAlchemyUoW(
                session=session,
                user_repo=UserRepositoryImpl(session=session)
            )

            yield uow

    def get_password_manager(self) -> PasswordManagerImpl:
        """
        Инициализация менеджера паролей
        """
        pass_manager = PasswordManagerImpl(
            pwd_context=self._pwd_context
        )

        return pass_manager


def get_service(
        uow: SQLAlchemyUoW = Depends(get_uow_stub),
        token_manager: AccessTokenManagerImpl = Depends(get_token_manager_stub),
        password_manager: PasswordManagerImpl = Depends(get_password_manager_stub)
) -> AuthService:
    """
    Инициализация сервиса
    """
    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    return auth_service
