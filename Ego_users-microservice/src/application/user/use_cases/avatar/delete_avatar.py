from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import AvatarUserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class DeleteAvatarData(UseCaseData):
    avatar_user_id: int

    class Config:
        frozen = True


class DeleteAvatar(BaseUseCase):
    """
    Сохранение аватара
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: DeleteAvatarData) -> dto.DeletedAvatarDTO:
        avatar = await self._uow.avatar_repo.get_avatar_by_user_id(
            avatar_user_id=AvatarUserId(value=data.avatar_user_id)
        )

        if avatar:
            avatar.delete()

        await self._uow.avatar_repo.delete_avatar(
            avatar_id=
            avatar.avatar_name
            if avatar
            else None
        )
        await self._uow.commit()

        deleted_avatar_dto = self._mapper.load(
            from_model=avatar,
            to_model=dto.DeletedAvatarDTO
        )

        return deleted_avatar_dto
