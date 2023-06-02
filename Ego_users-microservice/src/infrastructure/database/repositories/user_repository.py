from sqlalchemy import select
from asyncpg import UniqueViolationError  # type: ignore
from sqlalchemy.exc import IntegrityError, DBAPIError

from src.domain import UserAggregate
from src.application import UserRepo
from src.domain.user.value_objects import UserId
from src.infrastructure.database.models import Users
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.application.user.exceptions import (
    UserIsNotExist,
    UserIdIsAlreadyExist
)


class UserRepoImpl(SQLAlchemyRepo, UserRepo):
    """
    Реализация пользовательского репозитория
    """
    async def get_user_by_id(self, user_id: UserId) -> UserAggregate:
        """
        Получение пользователя по id
        """
        query = (
            select(Users)
            .where(Users.user_id == user_id.to_int)
            .with_for_update()
        )
        user = await self._session.execute(query)

        result = user.scalar()

        if not result:
            raise UserIsNotExist(user_id=user_id.to_int)

        user_aggregate = self._mapper.load(from_model=result, to_model=UserAggregate)

        return user_aggregate

    async def update_user(self, user: UserAggregate) -> None:
        """
        Обновление данных пользователя в базе
        """
        user_model = self._mapper.load(from_model=user, to_model=Users)
        try:
            await self._session.merge(user_model)
        except IntegrityError:
            pass

    async def create_user(self, user: UserAggregate) -> None:
        """
        Создание пользователя в базе
        """
        user_model = self._mapper.load(from_model=user, to_model=Users)

        self._session.add(user_model)

        try:
            await self._session.flush((user_model,))
        except IntegrityError as err:
            self._parse_error(err=err, user=user)

    @staticmethod
    def _parse_error(err: DBAPIError, user: UserAggregate) -> None:
        """
        определение ошибки
        """
        error = err.__cause__.__cause__.__class__  # type: ignore

        if error == UniqueViolationError:
            raise UserIdIsAlreadyExist(user_id=user.user_id.to_int)

