from src_users.application import SubscribeOnYourself
from src_users.application.common import BaseUseCase, Mapper, UseCaseData
from src_users.application.user import dto
from src_users.application.user.uow import UserUoW
from src_users.domain import SubscriptionEntity
from src_users.domain.user.value_objects import SubscriberId, SubscriptionId


class SubscribeData(UseCaseData):
    subscription_id: int
    subscriber_id: int

    class Config:
        frozen = True


class Subscribe(BaseUseCase):
    """
    Оформление подписки
    """

    def __init__(self, *, uow: UserUoW, mapper: Mapper) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: SubscribeData) -> dto.SubscribeActionDTO:
        if data.subscription_id == data.subscriber_id:
            raise SubscribeOnYourself()

        subscription = SubscriptionEntity.subscribe(
            subscription_id=SubscriptionId(value=data.subscription_id),
            subscriber_id=SubscriberId(value=data.subscriber_id),
        )
        await self._uow.subscription_repo.subscribe(subscription=subscription)
        await self._uow.commit()

        add_subscription_dto = self._mapper.load(
            from_model=subscription, to_model=dto.SubscribeActionDTO
        )

        return add_subscription_dto
