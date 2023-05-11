from abc import ABC, abstractmethod


class SubscriptionRepository(ABC):
    @abstractmethod
    def get_all_subscribers(self) -> list[Subscribers]:
        """Получаем всех подписчиков"""

    @abstractmethod
    def get_all_subscriptions(self) -> list[Subscriptions]:
        """Получаем все подписки"""

    @abstractmethod
    def subscribe(self) -> None:
        """Оформить подписку на пользователя"""

    @abstractmethod
    def unsubscribe(self) -> None:
        """Оформить отписку от пользователя"""
