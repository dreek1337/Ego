from sqlalchemy.ext.asyncio import AsyncSession

from src.common import RepositoryBase


class UserRepositoryBase(RepositoryBase):
    """
    Бызовый класс для репозитория пользователя
    """
    def __init__(self, session: AsyncSession):
        self._session = session
