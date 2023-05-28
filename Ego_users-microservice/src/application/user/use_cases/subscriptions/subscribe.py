from src.application.user import dto
from src.domain import SubscriptionEntity
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import (
    UserId,
    SubscriptionId, SubscriberId
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

    async def __call__(self, data: SubscribeData) -> dto.SubscribeDTO:
        subscription_user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.subscription_id)
        )
        subscriber_user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.subscriber_id)
        )

        subscription = SubscriptionEntity.subscribe(
            subscription_id=SubscriptionId(value=subscription_user.user_id.to_int),
            subscriber_id=SubscriberId(value=subscriber_user.user_id.to_int)
        )
        await self._uow.subscription_repo.subscribe(subscription=subscription)
        await self._uow.commit()

        add_subscription_dto = self._mapper.load(
            data=data,
            model=dto.SubscribeDTO
        )

        return add_subscription_dto
