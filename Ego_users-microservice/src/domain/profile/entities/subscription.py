from typing import Self
from dataclasses import dataclass


@dataclass
class BaseSubscriptionAndSubscriber:
    """
    Модель подписок/подписчиков
    """
    user_id: int
    first_name: str
    last_name: str

    @classmethod
    def create_subscriber(
            cls,
            *,
            user_id: int,
            first_name: str,
            last_name: str
    ) -> Self:
        """
        Создание модели подписчики/подписчика
        """
        subscription = BaseSubscriptionAndSubscriber(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name
        )

        return subscription

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class SubscriptionEntity(BaseSubscriptionAndSubscriber):
    """Создание модели подписки"""


class SubscriberEntity(BaseSubscriptionAndSubscriber):
    """Создание модели подписчика"""
