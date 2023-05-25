from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class GetSubscribersData(UseCaseData):
    user_id: int

    class Config:
        frozen = True


class GetSubscribers(BaseUseCase):
    """
    Получение всех подписчиков
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: GetSubscribersData) -> dto.SubscribersDTO:
        subscribers = await self._uow.subscription_repo.get_subscribers_by_id(
            user_id=UserId(value=data.user_id)
        )

        subscribers_dto = self._mapper.load(
            data=subscribers,
            model=dto.SubscribersDTO
        )

        return subscribers_dto
