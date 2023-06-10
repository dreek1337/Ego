from src.domain.common import Empty
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    BaseUseCase,
    UseCaseData
)
from src.application.user.interfaces import (
    GetSubscriptionsOrder,
    GetSubscriptionsFilters
)
from src.domain.user.value_objects import UserId


class GetSubscribersData(UseCaseData):
    user_id: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetSubscriptionsOrder = GetSubscriptionsOrder.ASC

    class Config:
        frozen = True


class GetSubscribers(BaseUseCase):
    """
    Получение всех подписчиков
    """
    def __init__(
            self,
            *,
            uow: UserUoW
    ) -> None:
        self._uow = uow

    async def __call__(self, data: GetSubscribersData) -> dto.SubscribersDTO:
        await self._uow.user_repo.get_user_by_id(user_id=UserId(value=data.user_id))

        subscribers = await self._uow.subscription_reader.get_subscribers_by_id(
            subscription_id=data.user_id,
            filters=GetSubscriptionsFilters(
                offset=data.offset,
                limit=data.limit,
                order=data.order
            )
        )

        return dto.SubscribersDTO(
            subscribers=subscribers,
            offset=data.offset,
            limit=data.limit
        )
