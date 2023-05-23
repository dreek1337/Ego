from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class DeleteAvatarData(UseCaseData):
    user_id: int

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
        await self._uow.avatar_repo.delete_avatar(user_id=UserId(value=data.user_id))
        await self._uow.commit()

        deleted_avatar_dto = self._mapper.load(data=data, model=dto.DeletedAvatarDTO)

        return deleted_avatar_dto
