from src.application import SubscriptionRepo
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.domain import (
    SubscriptionEntity,
    SubscriberEntity
)
from src.domain.user.value_objects import (
    UserId,
    SubscriptionId
)


class SubscriptionRepoImpl(SQLAlchemyRepo, SubscriptionRepo):
    async def get_subscriptions_by_id(
            self,
            user_id: UserId
    ) -> list[SubscriptionEntity]:
        return None  # type: ignore

    async def get_subscribers_by_id(
            self,
            user_id: UserId
    ) -> list[SubscriberEntity]:
        return None  # type: ignore

    async def add_subscribe(
            self,
            *,
            user_id: UserId,
            subscription_id: SubscriptionId
    ) -> None:
        pass

    async def delete_subscribe(
            self,
            *,
            user_id: UserId,
            subscription_id: SubscriptionId
    ) -> None:
        pass
