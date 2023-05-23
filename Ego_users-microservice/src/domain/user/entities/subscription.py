from typing import Self
from dataclasses import (
    dataclass,
    field
)

from src.domain.user.entities import AvatarEntity
from src.domain.user.value_objects import SubscriptionId


@dataclass
class BaseSubscriptionAndSubscriber:
    """
    Модель подписок/подписчиков
    """
    user_id: SubscriptionId
    first_name: str
    last_name: str
    avatar: AvatarEntity | None = field(default=None)

    @classmethod
    def create_subscriber(
            cls,
            *,
            user_id: SubscriptionId,
            first_name: str,
            last_name: str,
            avatar: AvatarEntity | None = None
    ) -> Self:
        """
        Создание модели подписчики/подписчика
        """
        subscription = BaseSubscriptionAndSubscriber(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar
        )

        return subscription


class SubscriptionEntity(BaseSubscriptionAndSubscriber):
    """Создание модели подписки"""


class SubscriberEntity(BaseSubscriptionAndSubscriber):
    """Создание модели подписчика"""
