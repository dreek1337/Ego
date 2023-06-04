import uuid

from pydantic import (
    UUID4,
    Field
)

from src.domain import AvatarEntity
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import (
    AvatarId,
    AvatarType,
    AvatarUserId
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class SetAvatarData(UseCaseData):
    avatar_user_id: int
    avatar_id: UUID4 = Field(uuid.uuid4(), description="Айди аватара")
    avatar_type: str
    avatar_content: bytes

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
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: SetAvatarData) -> dto.AvatarDTO:
        avatar = AvatarEntity.create_avatar(
            user_id=AvatarUserId(value=data.avatar_user_id),
            avatar_id=AvatarId(value=data.avatar_id),
            avatar_type=AvatarType(value=data.avatar_type),
            avatar_content=data.avatar_content
        )

        await self._uow.avatar_repo.set_avatar(avatar=avatar)
        await self._uow.commit()

        set_avatar_dto = self._mapper.load(from_model=avatar, to_model=dto.AvatarDTO)

        return set_avatar_dto
