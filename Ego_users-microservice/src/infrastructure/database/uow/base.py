from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.application import (
    CommitError,
    RollbackError
)


class SQLAlchemyBaseUoW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """
        Сохранение изменений в бд
        """
        try:
            await self._session.commit()
        except SQLAlchemyError as err:
            print()
            raise CommitError(content=err.args[0])

    async def rollback(self) -> None:
        """
        Откат изменений в бд
        """
        try:
            await self._session.rollback()
        except SQLAlchemyError as err:
            raise RollbackError(content=err.args[0])
