from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from src.application.exceptions import CommitError, RollbackError


class SQLAlchemyBaseUoW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """
        Применение коммита
        """
        try:
            await self._session.commit()
        except SQLAlchemyError as err:
            raise CommitError() from err

    async def rollback(self) -> None:
        """
        Применение ролбэка
        """
        try:
            await self._session.rollback()
        except SQLAlchemyError as err:
            raise RollbackError() from err
