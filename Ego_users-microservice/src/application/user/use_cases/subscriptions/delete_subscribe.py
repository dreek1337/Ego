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


class DeleteSubscriptionData(UseCaseData):
    user_id: int
    subscription_id: int

    class Config:
        frozen = True


class DeleteSubscription(BaseUseCase):
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

    async def __call__(self, data: DeleteSubscriptionData) -> dto.DeleteSubscriptionDTO:
        await self._uow.subscription_repo.delete_subscribe(
            user_id=UserId(value=data.user_id),
            subscription_id=SubscriptionId(value=data.subscription_id)
        )
        await self._uow.commit()

        delete_subscription_dto = self._mapper.load(
            data=data,
            model=dto.DeleteSubscriptionDTO
        )

        return delete_subscription_dto
