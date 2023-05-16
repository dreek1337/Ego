from abc import (
    ABC,
    abstractmethod
)


class SubscriptionRepo(ABC):
    """
    Репозиторий профиля
    """
    @abstractmethod
    async def subscribe(
            self,
            *,
            profile_id: int,
            subscriber_id: int
    ) -> None:
        """Подписаться на пользователя"""

    @abstractmethod
    async def unsubscribe(
            self,
            *,
            profile_id: int,
            subscriber_id: int
    ) -> None:
        """Отписаться от пользователя"""
