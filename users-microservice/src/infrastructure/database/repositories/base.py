from sqlalchemy.ext.asyncio import AsyncSession

from src.application import Mapper


class SQLAlchemyRepo:
    """
    Базовый класс для репозитория
    """
    def __init__(
            self,
            *,
            session: AsyncSession,
            mapper: Mapper
    ) -> None:
        self._session = session
        self._mapper = mapper
