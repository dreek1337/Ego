from src_users.application import AvatarIsNotExist
from src_users.application.common import BaseUseCase, Mapper, UseCaseData
from src_users.application.user import dto
from src_users.application.user.s3 import UserCloudStorage
from src_users.application.user.uow import UserUoW
from src_users.domain.user.value_objects import AvatarUserId


class DeleteAvatarData(UseCaseData):
    avatar_user_id: int

    class Config:
        frozen = True


class DeleteAvatar(BaseUseCase):
    """
    Сохранение аватара
    """

    def __init__(
        self, *, uow: UserUoW, mapper: Mapper, cloud_storage: UserCloudStorage
    ) -> None:
        self._uow = uow
        self._mapper = mapper
        self._cloud_storage = cloud_storage

    async def __call__(self, data: DeleteAvatarData) -> dto.DeletedAvatarDTO:
        avatar = await self._uow.avatar_repo.get_avatar_by_user_id(
            avatar_user_id=AvatarUserId(value=data.avatar_user_id)
        )

        if not avatar:
            raise AvatarIsNotExist()

        avatar.delete()

        avatar_id = avatar.avatar_id

        await self._uow.avatar_repo.delete_avatar(avatar_id=avatar_id)  # type: ignore
        await self._cloud_storage.delete(avatar=avatar)
        await self._uow.commit()

        deleted_avatar_dto = self._mapper.load(
            from_model=avatar, to_model=dto.DeletedAvatarDTO
        )

        return deleted_avatar_dto
