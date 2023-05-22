from abc import (
    ABC,
    abstractmethod
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
    async def subscribe(
            self,
            *,
            user_id: UserId,
            subscriber_id: SubscriptionId
    ) -> None:
        """Подписаться на пользователя"""

    @abstractmethod
    async def unsubscribe(
            self,
            *,
            user_id: UserId,
            subscriber_id: SubscriptionId
    ) -> None:
        """Отписаться от пользователя"""
