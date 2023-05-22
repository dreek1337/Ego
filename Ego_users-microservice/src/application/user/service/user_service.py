from src.application.user import dto
from src.application.common import Mapper
from src.application.user.uow import UserUoW
from src.application.user.use_cases import (
    CreateUserData,
    CreateUser,
    DeleteUserData,
    DeleteUser,
    UpdateUserData,
    UpdateUser
)


class UserService:
    """
    Сервис который отвечает за работу с Пользователем
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._uow = uow
        self._mapper = mapper

    async def create_profile(self, data: CreateUserData) -> dto.CreatedUserDTO:
        return await CreateUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_profile(self, data: DeleteUserData) -> dto.DeletedUserDTO:
        return await DeleteUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def update_profile(self, data: UpdateUserData) -> dto.UpdatedUser:
        return await UpdateUser(uow=self._uow, mapper=self._mapper)(data=data)
