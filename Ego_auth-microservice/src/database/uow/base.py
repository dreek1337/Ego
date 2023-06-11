from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyBaseUoW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """
        Применение коммита
        """
        try:
            await self._session.commit()
        except Exception:
            # raise CommitError()
            pass

    async def rollback(self) -> None:
        """
        Применение ролбэка
        """
        try:
            await self._session.rollback()
        except Exception:
            # raise RollbackError()
            pass
