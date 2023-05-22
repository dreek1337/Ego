from pydantic import BaseModel

from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class DeleteUserData(UseCaseData):
    user_id: int

    class Config:
        frozen = True


class DeleteUser(BaseUseCase):
    """
    Удаление пользователя
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: DeleteUserData) -> dto.DeletedUserDTO:
        user = await self._uow.user_repo.get_user_by_id(user_id=UserId(value=data.user_id))

        user.delete_user()
        await self._uow.user_repo.update_user(user=user)
        await self._uow.commit()

        user_dto = self._mapper.load(data=user, model=dto.DeletedUserDTO)

        return user_dto
