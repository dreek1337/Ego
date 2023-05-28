from dataclasses import dataclass

from src.domain.common import Entity
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId
)


@dataclass
class SubscriptionEntity(Entity):
    """
    Модель подписок
    """
    subscription_user_id: SubscriptionId
    subscriber_user_id: SubscriberId

    @classmethod
    def subscribe(
            cls,
            *,
            subscription_id: SubscriptionId,
            subscriber_id: SubscriberId
    ) -> 'SubscriptionEntity':
        """
        Создание модели подписки
        """
        subscription = SubscriptionEntity(
            subscription_user_id=subscription_id,
            subscriber_user_id=subscriber_id
        )

        return subscription
