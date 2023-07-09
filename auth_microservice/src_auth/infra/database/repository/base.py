from sqlalchemy.ext.asyncio import AsyncSession


class UserRepositoryBase:
    """
    Бызовый класс для репозитория пользователя
    """

    def __init__(self, session: AsyncSession):
        self._session = session
