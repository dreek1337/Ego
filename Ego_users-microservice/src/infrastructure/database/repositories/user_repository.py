from sqlalchemy import select
from asyncpg import UniqueViolationError  # type: ignore
from sqlalchemy.exc import (
    DBAPIError,
    IntegrityError
)

from src.domain import UserAggregate
from src.application import UserRepo, RepoError
from src.domain.user.value_objects import UserId
from src.infrastructure.database.models import Users
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.infrastructure.database.error_interceptor import error_interceptor
from src.application.user.exceptions import (
    UserIsNotExist,
    UserIdIsAlreadyExist
)


class UserRepoImpl(SQLAlchemyRepo, UserRepo):
    """
    Реализация пользовательского репозитория
    """
    @error_interceptor(file_name=__name__)
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

    @error_interceptor(file_name=__name__)
    async def update_user(self, user: UserAggregate) -> None:
        """
        Обновление данных пользователя в базе
        """
        user_model = self._mapper.load(from_model=user, to_model=Users)

        await self._session.merge(user_model)

    @error_interceptor(file_name=__name__)
    async def create_user(self, user: UserAggregate) -> None:
        """
        Создание пользователя в базе
        """
        user_model = self._mapper.load(from_model=user, to_model=Users)

        self._session.add(user_model)

        try:
            await self._session.flush((user_model,))
        except IntegrityError as err:
            self._parse_error(err=err, data=user)

    @staticmethod
    def _parse_error(
            err: DBAPIError,
            data: UserAggregate
    ) -> None:
        """
        Определение ошибки
        """
        error = err.__cause__.__cause__.__class__  # type: ignore

        if error == UniqueViolationError:
            raise UserIdIsAlreadyExist(user_id=data.user_id.to_int)
        else:
            raise RepoError() from err
