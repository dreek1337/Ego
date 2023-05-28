from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    select,
    delete
)

from src.domain import AvatarEntity
from src.application import AvatarRepo
from src.domain.user.value_objects import AvatarId
from src.infrastructure.database.models import Avatars
from src.infrastructure.database.repositories.base import SQLAlchemyRepo


class AvatarRepoImpl(SQLAlchemyRepo, AvatarRepo):
    """
    Реализация репозитория аватарки
    """
    async def get_avatar_by_id(self, avatar_id: AvatarId) -> AvatarEntity:
        """
        Получение аватарки по ее айди
        """
        query = (
            select(Avatars)
            .where(Avatars.avatar_id == avatar_id.to_uuid)
        )

        avatar = await self._session.scalar(query)

        if not avatar:
            # raise AvatarIsNotExist(avatar_id.to_uuid)
            pass

        avatar_entity = self._mapper.load(avatar, AvatarEntity)

        return avatar_entity

    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """
        Установка аватарки пользователю
        """
        avatar_model = self._mapper.load(avatar, Avatars)

        self._session.add(avatar_model)

        try:
            await self._session.flush((avatar_model,))
        except IntegrityError:
            pass  # Добавить обрабокту ошибок

    async def update_avatar(self, avatar: AvatarEntity) -> None:
        """
        Обнавление аватарки пользователя
        """
        avatar_model = self._mapper.load(avatar, Avatars)

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
