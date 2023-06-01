from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.domain import UserAggregate
from src.application import UserRepo
from src.domain.user.value_objects import UserId
from src.infrastructure.database.models import Users
from src.infrastructure.database.repositories.base import SQLAlchemyRepo


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
            # raise UserIsNotExist(user_id.to_int)
            pass

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
            pass  # Добавить обрабокту ошибок

    async def create_user(self, user: UserAggregate) -> None:
        """
        Создание пользователя в базе
        """
        user_model = self._mapper.load(from_model=user, to_model=Users)

        self._session.add(user_model)

        try:
            await self._session.flush((user_model,))
        except IntegrityError:
            pass  # Добавить обрабокту ошибок
