from abc import (
    ABC,
    abstractmethod
)

from src.domain.user import (
    SubscriberEntity,
    SubscriptionEntity
)
from src.domain.user.value_objects import (
    UserId,
    SubscriptionId
)


class SubscriptionRepo(ABC):
    """
    Репозиторий подпичок
    """
    @abstractmethod
    async def get_subscriptions_by_id(self, user_id: UserId) -> list[SubscriptionEntity]:
        """Получение подписок"""

    @abstractmethod
    async def get_subscribers_by_id(self, user_id: UserId) -> list[SubscriberEntity]:
        """Получение подписчиков"""

    @abstractmethod
    async def add_subscribe(
            self,
            *,
            user_id: UserId,
            subscription_id: SubscriptionId
    ) -> None:
        """Подписаться на пользователя"""

    @abstractmethod
    async def delete_subscribe(
            self,
            *,
            user_id: UserId,
            subscription_id: SubscriptionId
    ) -> None:
        """Отписаться от пользователя"""
