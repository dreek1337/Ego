from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyBaseUoW:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """
        Сохранение изменений в бд
        """
        await self._session.commit()

    async def rollback(self) -> None:
        """
        Откат изменений в бд
        """
        await self._session.rollback()
