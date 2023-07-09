from typing import (
    Any,
    TypeVar,
)

from asyncpg import UniqueViolationError  # type: ignore
from sqlalchemy import select
from sqlalchemy.exc import (
    DBAPIError,
    IntegrityError,
)
from src_auth.application.exceptions import (
    RepoError,
    UserDataIsNotCorrect,
    UserIsNotExists,
    UsernameIsAlreadyExist,
)
from src_auth.common import UserRepo
from src_auth.config.schemas.user_models import (
    UserModel,
    UserSaveDataInDB,
)

from ..exception_incepter import error_interceptor
from ..models import Users
from .base import UserRepositoryBase

DataModel = TypeVar("DataModel", bound=Any)


class UserRepositoryImpl(UserRepositoryBase, UserRepo):
    """
    Реализация репозитория для работы с моделю пользователя
    """

    @error_interceptor
    async def get_user_by_id(self, user_id: int) -> UserModel:
        """
        Получение пользователя по айли
        """
        query = select(Users).where(Users.user_id == user_id)

        user = await self._session.execute(query)

        result = user.scalar()

        if not result:
            raise UserIsNotExists(user_id=user_id)

        return UserModel.from_orm(result)

    @error_interceptor
    async def get_user_by_username(self, username: str) -> UserModel:
        """
        Получение пользователя по никнейму
        """
        query = select(Users).where(Users.username == username)

        user = await self._session.execute(query)

        result = user.scalar()

        if not result:
            raise UserDataIsNotCorrect()

        return UserModel.from_orm(result)

    @error_interceptor
    async def create_user(self, data: UserSaveDataInDB) -> None:
        """
        Создание пользователя и возвращение его айди
        """
        user = Users(
            username=data.username,
            password=data.password,
            user_email=data.user_email,
            salt=data.salt,
        )
        self._session.add(user)

        try:
            await self._session.flush((user,))
        except IntegrityError as err:
            self._parse_error(err=err, data=data)

    @error_interceptor
    async def update_user(self, data: UserModel) -> None:
        """
        Обнавление данных пользователя
        """
        user = Users(
            username=data.username,
            password=data.password,
            user_email=data.user_email,
            salt=data.salt,
        )

        await self._session.merge(user)

    @staticmethod
    def _parse_error(err: DBAPIError, data: DataModel) -> None:
        """
        Определение ошибки
        """
        error = err.__cause__.__cause__.__class__  # type: ignore

        if error == UniqueViolationError:
            raise UsernameIsAlreadyExist(username=data.username)
        else:
            raise RepoError() from err
