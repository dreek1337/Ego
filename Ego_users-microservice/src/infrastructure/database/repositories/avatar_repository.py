from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    select,
    delete
)

from src.domain import AvatarEntity
from src.application import AvatarRepo
from src.infrastructure.database.models import Avatars
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.domain.user.value_objects import (
    AvatarId,
    AvatarUserId
)


class AvatarRepoImpl(SQLAlchemyRepo, AvatarRepo):
    """
    Реализация репозитория аватарки
    """
    async def get_avatar_by_user_id(self, avatar_user_id: AvatarUserId) -> AvatarEntity:
        """
        Получение аватарки по ее айди
        """
        query = (
            select(Avatars)
            .where(Avatars.avatar_user_id == avatar_user_id.to_int)
        )

        avatar = await self._session.execute(query)

        if avatar:
            # raise AvatarIsNotExist(avatar_user_id.to_int)
            avatar = avatar.scalar()  # type: ignore
        # Сделать что-то с моделью, которая будет None,
        # может перенести проверку в маппер
        avatar_entity = self._mapper.load(from_model=avatar, to_model=AvatarEntity)

        return avatar_entity

    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """
        Установка аватарки пользователю
        """
        avatar_model = self._mapper.load(from_model=avatar, to_model=Avatars)

        self._session.add(avatar_model)

        try:
            await self._session.flush((avatar_model,))
        except IntegrityError:
            pass  # Добавить обрабокту ошибок

    async def update_avatar(self, avatar: AvatarEntity) -> None:
        """
        Обнавление аватарки пользователя
        """
        avatar_model = self._mapper.load(from_model=avatar, to_model=Avatars)

        try:
            await self._session.merge(avatar_model)
        except IntegrityError:
            pass  # Добавить обрабокту ошибок

    async def delete_avatar(self, avatar_id: AvatarId) -> None:
        """
        Удаление аватарки по айди
        """
        query = (
            delete(Avatars)
            .where(Avatars.avatar_id == avatar_id.to_uuid)
        )

        await self._session.execute(query)
