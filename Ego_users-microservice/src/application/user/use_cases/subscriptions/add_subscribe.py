from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import (
    UserId,
    SubscriptionId
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class AddSubscriptionData(UseCaseData):
    user_id: int
    subscription_id: int

    class Config:
        frozen = True


class AddSubscription(BaseUseCase):
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

    async def __call__(self, data: AddSubscriptionData) -> dto.AddSubscriptionDTO:
        await self._uow.subscription_repo.add_subscribe(
            user_id=UserId(value=data.user_id),
            subscription_id=SubscriptionId(value=data.subscription_id)
        )
        await self._uow.commit()

        add_subscription_dto = self._mapper.load(
            data=data,
            model=dto.AddSubscriptionDTO
        )

        return add_subscription_dto
