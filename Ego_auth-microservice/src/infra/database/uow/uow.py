from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.uow.base import SQLAlchemyBaseUoW
from src.infra import UserRepositoryImpl


class SQLAlchemyUoW(SQLAlchemyBaseUoW):
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
