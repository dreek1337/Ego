from src.domain.common import Empty
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UpdateAvatarData(UseCaseData):
    user_id: int
    avatar_type: str | Empty = Empty.UNSET
    avatar_content: bytes | Empty = Empty.UNSET

    class Config:
        frozen = True


class UpdateAvatar(BaseUseCase):
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

    async def __call__(self, data: UpdateAvatarData) -> dto.UpdatedAvatarDTO:
        avatar = await self._uow.avatar_repo.get_avatar_by_id(user_id=UserId(value=data.user_id))

        avatar.update_avatar(
            avatar_type=data.avatar_type,
            avatar_content=data.avatar_content
        )
        await self._uow.avatar_repo.update_avatar(avatar=avatar)
        await self._uow.commit()

        updated_avatar_dto = self._mapper.load(data=avatar, model=dto.UpdatedAvatarDTO)

        return updated_avatar_dto
