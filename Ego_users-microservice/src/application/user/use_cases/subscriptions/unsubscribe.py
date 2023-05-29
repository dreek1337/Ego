from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UnsubscribeData(UseCaseData):
    subscription_id: int
    subscriber_id: int

    class Config:
        frozen = True


class Unsubscribe(BaseUseCase):
    """
    Удаление подписки
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: UnsubscribeData) -> dto.UnsubscribeDTO:
        subscription = await self._uow.subscription_repo.get_subscription_by_id(
            subscription_id=SubscriptionId(value=data.subscription_id),
            subscriber_id=SubscriberId(value=data.subscriber_id)
        )

        await self._uow.subscription_repo.unsubscribe(subscription=subscription)
        await self._uow.commit()

        delete_subscription_dto = self._mapper.load(
            from_model=data,
            to_model=dto.UnsubscribeDTO
        )

        return delete_subscription_dto
