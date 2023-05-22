from pydantic import UUID4
from src.domain import AvatarEntity
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)
from src.domain.user.value_objects import (
    AvatarId,
    AvatarType
)


class DeleteAvatarData(UseCaseData):
    avatar_id: UUID4

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
        await self._uow.avatar_repo.delete_avatar(avatar_id=AvatarId(value=data.avatar_id))
        await self._uow.commit()

        avatar_dto = self._mapper.load(data=data, model=dto.DeletedAvatarDTO)

        return avatar_dto
