from src.application.common import DTO
from src.application.user.dto.subscription.subscription_data import Subscription


class Subscriptions(DTO):
    """
    Модель подписок
    """
    users: list[Subscription]

    class Config:
        frozen = True
