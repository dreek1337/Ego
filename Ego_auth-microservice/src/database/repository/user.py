from typing import Any

from sqlalchemy import select

from src.database.models import Users
from src.database.repository.base import UserRepositoryBase


class UserRepositoryImpl(UserRepositoryBase):
    async def get_user_by_id(self, user_id: int) -> Any:
        """
        Получение пользователя по айди
        """
        query = (
            select(Users)
            .where(Users.user_id == user_id)
        )

        await self._session.execute(query)

        # сделать маппер если нужен

    async def create_user(self, data) -> None:
        """
        Создание пользователя
        """
        user = data
        self._session.add(user)

        await self._session.flush((user,))

    async def update_user(self) -> None:
        pass

    async def delete_user(self) -> None:
        pass
