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


class GetSubscriptionsData(UseCaseData):
    subscriber_id: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetSubscriptionsOrder = GetSubscriptionsOrder.ASC

    class Config:
        frozen = True


class GetSubscriptions(BaseUseCase):
    """
    Получение всех подписчиков
    """
    def __init__(
            self,
            *,
            uow: UserUoW
    ) -> None:
        self._uow = uow

    async def __call__(self, data: GetSubscriptionsData) -> dto.SubscriptionsDTO:
        subscriptions = await self._uow.subscription_reader.get_subscriptions_by_id(
            subscriber_id=data.subscriber_id,
            filters=GetSubscriptionsFilters(
                offset=data.offset,
                limit=data.limit,
                order=data.order
            )
        )

        return dto.SubscriptionsDTO(
            subscriptions=subscriptions,
            offset=data.offset,
            limit=data.limit
        )
