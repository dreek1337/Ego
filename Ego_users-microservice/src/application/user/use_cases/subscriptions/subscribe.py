from src.application.user import dto
from src.domain import SubscriptionEntity
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId,
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class SubscribeData(UseCaseData):
    subscription_id: int
    subscriber_id: int

    class Config:
        frozen = True


class Subscribe(BaseUseCase):
    """
    Оформление подписки
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: SubscribeData) -> dto.SubscribeActionDTO:
        subscription = SubscriptionEntity.subscribe(
            subscription_id=SubscriptionId(value=data.subscription_id),
            subscriber_id=SubscriberId(value=data.subscriber_id)
        )
        await self._uow.subscription_repo.subscribe(subscription=subscription)
        await self._uow.commit()

        add_subscription_dto = self._mapper.load(
            from_model=subscription,
            to_model=dto.SubscribeActionDTO
        )

        return add_subscription_dto
