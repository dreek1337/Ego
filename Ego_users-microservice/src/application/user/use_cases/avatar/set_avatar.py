import uuid

from pydantic import (
    UUID4,
    Field
)

from src.domain import AvatarEntity
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import CloudStorageBase
from src.domain.user.exceptions import UserIsDeleted
from src.application.user.exceptions import UserIsNotExist
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)
from src.domain.user.value_objects import (
    AvatarId,
    AvatarType,
    AvatarUserId, UserId
)


class SetAvatarData(UseCaseData):
    avatar_type: str
    avatar_user_id: int
    avatar_content: bytes
    avatar_id: UUID4 = Field(uuid.uuid4(), description="Айди аватара")

    class Config:
        frozen = True


class SetAvatar(BaseUseCase):
    """
    Сохранение аватара
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper,
            cloud_storage: CloudStorageBase
    ) -> None:
        self._uow = uow
        self._mapper = mapper
        self._cloud_storage = cloud_storage

    async def __call__(self, data: SetAvatarData) -> dto.AvatarDTO:
        user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.avatar_user_id)
        )

        if user:
            raise UserIsNotExist(user_id=data.avatar_user_id)
        if user.deleted:
            raise UserIsDeleted(user_id=data.avatar_user_id)

        avatar = AvatarEntity.create_avatar(
            avatar_user_id=AvatarUserId(value=data.avatar_user_id),
            avatar_name=AvatarId(value=data.avatar_id),
            avatar_type=AvatarType(value=data.avatar_type)
        )

        await self._uow.avatar_repo.set_avatar(avatar=avatar)
        await self._cloud_storage.put(data=data)

        await self._uow.commit()

        set_avatar_dto = self._mapper.load(from_model=avatar, to_model=dto.AvatarDTO)

        return set_avatar_dto
