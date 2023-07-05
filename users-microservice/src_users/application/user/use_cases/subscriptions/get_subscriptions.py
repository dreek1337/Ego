from src_users.application.common import BaseUseCase, UseCaseData
from src_users.application.user import dto
from src_users.application.user.interfaces import (
    GetSubscriptionsFilters,
    GetSubscriptionsOrder,
)
from src_users.application.user.uow import UserUoW
from src_users.domain.common import Empty
from src_users.domain.user.value_objects import UserId


class GetSubscriptionsData(UseCaseData):
    user_id: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetSubscriptionsOrder = GetSubscriptionsOrder.ASC

    class Config:
        frozen = True


class GetSubscriptions(BaseUseCase):
    """
    Получение всех подписчиков
    """

    def __init__(self, *, uow: UserUoW) -> None:
        self._uow = uow

    async def __call__(self, data: GetSubscriptionsData) -> dto.SubscriptionsDTO:
        await self._uow.user_repo.get_user_by_id(user_id=UserId(value=data.user_id))

        subscriptions = await self._uow.subscription_reader.get_subscriptions_by_id(
            subscriber_id=data.user_id,
            filters=GetSubscriptionsFilters(
                offset=data.offset, limit=data.limit, order=data.order
            ),
        )

        return dto.SubscriptionsDTO(
            subscriptions=subscriptions, offset=data.offset, limit=data.limit
        )
