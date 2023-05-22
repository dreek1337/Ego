from src.application.common import DTO
from src.application.user.dto.subscription.subscription_data import Subscriber


class Subscribers(DTO):
    """
    Модель подписчиков
    """
    users: list[Subscriber]

    class Config:
        frozen = True
