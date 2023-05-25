import uuid

from pydantic import (
    UUID4,
    Field
)

from src.domain import AvatarEntity
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)
from src.domain.user.value_objects import (
    UserId,
    AvatarId,
    AvatarType
)


class SetAvatarData(UseCaseData):
    avatar_id: UUID4 = Field(uuid.uuid4(), description="Айди аватара")
    avatar_type: str
    avatar_content: bytes
    user_id: int

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

    async def __call__(self, data: SetAvatarData) -> dto.SetAvatarDTO:
        avatar = AvatarEntity.create_avatar(
            avatar_id=AvatarId(value=data.avatar_id),
            avatar_type=AvatarType(value=data.avatar_type),
            avatar_content=data.avatar_content
        )

        await self._uow.avatar_repo.set_avatar(
            user_id=UserId(value=data.user_id),
            avatar=avatar
        )
        await self._uow.commit()

        set_avatar_dto = self._mapper.load(data=avatar, model=dto.SetAvatarDTO)

        return set_avatar_dto
