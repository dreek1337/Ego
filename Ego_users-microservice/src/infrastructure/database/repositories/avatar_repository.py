from sqlalchemy import (
    select,
    delete
)
from sqlalchemy.exc import IntegrityError

from src.domain import AvatarEntity
from src.infrastructure.database.models import Avatars
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.infrastructure.database.error_interceptor import error_interceptor
from src.application import (
    AvatarRepo,
    AvatarIsNotExist
)
from src.domain.user.value_objects import (
    AvatarId,
    AvatarUserId
)


class AvatarRepoImpl(SQLAlchemyRepo, AvatarRepo):
    """
    Реализация репозитория аватарки
    """
    @error_interceptor(file_name=__name__)
    async def get_avatar_by_user_id(
            self,
            avatar_user_id: AvatarUserId
    ) -> AvatarEntity | None:
        """
        Получение аватарки по ее айди
        """
        query = (
            select(Avatars)
            .where(Avatars.avatar_user_id == avatar_user_id.to_int)
        )
        avatar = await self._session.execute(query)

        result = avatar.scalar()

        if not result:
            return result  # type: ignore

        avatar_entity = self._mapper.load(from_model=result, to_model=AvatarEntity)

        return avatar_entity

    @error_interceptor(file_name=__name__)
    async def set_avatar(self, avatar: AvatarEntity) -> None:
        """
        Сохранение данных об аватарке или их обнавление
        """
        avatar_model = self._mapper.load(from_model=avatar, to_model=Avatars)
        query = (
            delete(Avatars)
            .where(Avatars.avatar_user_id == avatar.avatar_user_id.to_int)
        )

        await self._session.execute(query)

        self._session.add(avatar_model)

        try:
            await self._session.flush((avatar_model,))
        except IntegrityError as err:
            self._parse_error(err=err, data=avatar)

    @error_interceptor(file_name=__name__)
    async def delete_avatar(self, avatar_id: AvatarId | None) -> None:
        """
        Удаление аватарки по айди
        """
        if not avatar_id:
            raise AvatarIsNotExist()

        query = (
            delete(Avatars)
            .where(Avatars.avatar_id == avatar_id.to_uuid)
        )

        await self._session.execute(query)
