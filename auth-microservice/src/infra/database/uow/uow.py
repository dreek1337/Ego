from sqlalchemy.ext.asyncio import AsyncSession
from src.application.auth_uow import AuthUoW
from src.infra import UserRepositoryImpl

from .base import SQLAlchemyBaseUoW


class SQLAlchemyUoW(SQLAlchemyBaseUoW, AuthUoW):
    """
    реализация uow
    """
    def __init__(
            self,
            *,
            session: AsyncSession,
            user_repo: UserRepositoryImpl) -> None:
        self.user_repo = user_repo

        super().__init__(session=session)
