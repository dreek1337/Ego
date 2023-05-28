from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class GetUserData(UseCaseData):
    user_id: int

    class Config:
        frozen = True


class GetUser(BaseUseCase):
    """
    Получение пользователя
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: GetUserData) -> dto.UserDTO:
        user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.user_id)
        )
        subscribers = await self._uow.subscription_reader.get_count_subscribers(
            subscription_id=user.user_id.to_int
        )
        subscriptions = await self._uow.subscription_reader.get_count_subscriptions(
            subscriber_id=user.user_id.to_int
        )

        user.set_count_of_subscribers(count_of_subscribers=subscribers)
        user.set_count_of_subscriptions(count_of_subscriptions=subscriptions)

        profile_dto = self._mapper.load(data=user, model=dto.UserDTO)

        return profile_dto
