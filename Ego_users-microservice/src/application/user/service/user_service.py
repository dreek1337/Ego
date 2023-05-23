from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    Mapper,
    Service
)
from src.application.user import use_cases


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

    async def get_profile(self, data: use_cases.GetUserData) -> dto.UserDTO:
        return await use_cases.GetUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def create_profile(self, data: use_cases.CreateUserData) -> dto.CreatedUserDTO:
        return await use_cases.CreateUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def update_profile(self, data: use_cases.UpdateUserData) -> dto.UpdatedUserDTO:
        return await use_cases.UpdateUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_profile(self, data: use_cases.DeleteUserData) -> dto.DeletedUserDTO:
        return await use_cases.DeleteUser(uow=self._uow, mapper=self._mapper)(data=data)

    async def set_avatar(self, data: use_cases.SetAvatarData) -> dto.SetAvatarDTO:
        return await use_cases.SetAvatar(uow=self._uow, mapper=self._mapper)(data=data)

    async def update_avatar(self, data: use_cases.UpdateAvatarData) -> dto.UpdatedAvatarDTO:
        return await use_cases.UpdateAvatar(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_avatar(self, data: use_cases.DeleteAvatarData) -> dto.DeletedAvatarDTO:
        return await use_cases.DeleteAvatar(uow=self._uow, mapper=self._mapper)(data=data)

    async def add_subscribe(self, data: use_cases.AddSubscriptionData) -> dto.AddSubscriptionDTO:
        return await use_cases.AddSubscription(uow=self._uow, mapper=self._mapper)(data=data)

    async def get_subscribers(self, data: use_cases.GetSubscribersData) -> dto.SubscribersDTO:
        return await use_cases.GetSubscribers(uow=self._uow, mapper=self._mapper)(data=data)

    async def get_subscriptions(self, data: use_cases.GetSubscriptionsData) -> dto.SubscriptionsDTO:
        return await use_cases.GetSubscriptions(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_subscribe(self, data: use_cases.DeleteSubscriptionData) -> dto.DeleteSubscriptionDTO:
        return await use_cases.DeleteSubscription(uow=self._uow, mapper=self._mapper)(data=data)
