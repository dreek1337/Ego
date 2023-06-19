from abc import (
    ABC,
    abstractmethod
)

from src.domain.user import SubscriptionEntity
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId
)


class SubscriptionRepo(ABC):
    """
    Репозиторий подпичок
    """
    @abstractmethod
    async def get_subscription_by_id(
            self,
            *,
            subscription_id: SubscriptionId,
            subscriber_id: SubscriberId
    ) -> SubscriptionEntity:
        """Получение подписки"""

    @abstractmethod
    async def subscribe(self, subscription: SubscriptionEntity) -> None:
        """Подписаться на пользователя"""

    @abstractmethod
    async def unsubscribe(self, subscription: SubscriptionEntity) -> None:
        """Отписаться от пользователя"""
