from dataclasses import dataclass

from src.domain.models.value_objects.subscription_value_objects import (
    SubscriptionId,
    SubscriptionName
)


@dataclass
class Subscription:
    """
    Модель подписок
    """
    user_id: SubscriptionId
    username: SubscriptionName
