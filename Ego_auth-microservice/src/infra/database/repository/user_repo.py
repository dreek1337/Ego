from sqlalchemy import select

from src.infra.database.models import Users
from src.common import RepositoryBase
from src.infra.database.repository.base import UserRepositoryBase
from src.config import (
    UserModel,
    UserSaveDataInDB
)


class UserRepositoryImpl(UserRepositoryBase, RepositoryBase):
    """
    Реализация репозитория для работы с моделю пользователя
    """
    async def get_user_by_username(self, username: str) -> UserModel:
        """
        Получение пользователя по айди
        """
        query = (
            select(Users)
            .where(Users.username == username)
        )

        user = await self._session.execute(query)

        result = user.scalar()

        if not result:
            raise Exception

        return UserModel.from_orm(result)

    async def create_user(self, data: UserSaveDataInDB) -> None:
        """
        Создание пользователя и возвращение его айди
        """
        user = Users(
            usermame=data.username,
            password=data.password,
            user_email=data.user_email
        )
        self._session.add(user)

        try:
            await self._session.flush((user,))
        except Exception as err:
            self._parse_error(err=err, data=data)

    async def update_user(self, data: UserModel) -> None:
        """
        Обнавление данных пользователя
        """
        user = Users(**data.dict())

        await self._session.merge(user)

    def _parse_error(self, err, data) -> None:
        pass
