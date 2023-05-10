from dataclasses import dataclass

from src.domain.models.value_objects import (
    SubscriberId,
    SubscriberName
)

@dataclass
class Subscriber:
    """
    Модель подписчика
    """
    user_id: SubscriberId
    username: SubscriberName
