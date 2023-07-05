from src_users.application.common import BaseUseCase, Mapper, UseCaseData
from src_users.application.user import dto
from src_users.application.user.uow import UserUoW
from src_users.domain.user.value_objects import UserId


class DeleteUserData(UseCaseData):
    user_id: int

    class Config:
        frozen = True


class DeleteUser(BaseUseCase):
    """
    Удаление пользователя
    """

    def __init__(self, *, uow: UserUoW, mapper: Mapper) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: DeleteUserData) -> dto.DeletedUserDTO:
        user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.user_id)
        )

        user.delete_user()
        await self._uow.user_repo.update_user(user=user)
        await self._uow.commit()

        deleted_user_dto = self._mapper.load(
            from_model=user, to_model=dto.DeletedUserDTO
        )

        return deleted_user_dto
