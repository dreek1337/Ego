from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.common import (
    Empty,
    ValidAvatarType
)
from src.domain.user.value_objects import (
    AvatarType,
    AvatarUserId
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UpdateAvatarData(UseCaseData):
    avatar_user_id: int
    avatar_type: ValidAvatarType | Empty = Empty.UNSET
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

    async def __call__(self, data: UpdateAvatarData) -> dto.AvatarDTO | None:
        avatar = await self._uow.avatar_repo.get_avatar_by_user_id(
            avatar_user_id=AvatarUserId(value=data.avatar_user_id)
        )

        if not avatar:
            return avatar  # type: ignore

        avatar_type: AvatarType | Empty = (
            AvatarType(value=data.avatar_type)
            if data.avatar_type is not Empty.UNSET
            else Empty.UNSET
        )

        avatar.update_avatar(
            avatar_type=avatar_type,
            avatar_content=data.avatar_content
        )
        await self._uow.avatar_repo.update_avatar(avatar=avatar)
        await self._uow.commit()

        updated_avatar_dto = self._mapper.load(
            from_model=avatar,
            to_model=dto.AvatarDTO
        )

        return updated_avatar_dto
