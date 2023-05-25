from sqlalchemy import select

from src.application import UserRepo
from src.domain import UserAggregate
from src.domain.user.value_objects import UserId
from src.infrastructure.database.models import Users, Avatars
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
            select(Users, Avatars.avatar_content)
            .join(Users.avatar, isouter=True)
            .where(Users.user_id == user_id.to_int)
        )
        user = await self._session.scalars(query)

        user_entity = self._mapper.load(data=user, model=UserAggregate)

        return user_entity

    async def update_user(self, user: UserAggregate) -> None:
        pass

    async def create_user(self, user: UserAggregate) -> None:
        pass
