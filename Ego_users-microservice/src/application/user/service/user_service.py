from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    Mapper,
    Service
)
from src.application.user.use_cases import (
    SetAvatar,
    SetAvatarData,
    DeleteAvatar,
    DeleteAvatarData,
    CreateUser,
    CreateUserData,
    DeleteUser,
    DeleteUserData,
    UpdateUser,
    UpdateUserData,
)


class UserService(Service):
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

    async def get_profile(self):
        pass

    async def create_profile(self, data: CreateUserData) -> dto.CreatedUserDTO:
        return await CreateUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def update_profile(self, data: UpdateUserData) -> dto.UpdatedUserDTO:
        return await UpdateUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_profile(self, data: DeleteUserData) -> dto.DeletedUserDTO:
        return await DeleteUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def set_avatar(self, data: SetAvatarData) -> dto.SetAvatarDTO:
        return await SetAvatar(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_avatar(self, data: DeleteAvatarData) -> dto.DeletedAvatarDTO:
        return await DeleteAvatar(uow=self._uow, mapper=self._mapper)(data=data)
