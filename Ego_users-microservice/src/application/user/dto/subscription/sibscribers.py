from src.application.common import DTO
from src.application.user.dto.subscription.subscriptiondto import SubscriptionDTO


class SubscribersDTO(DTO):
    """
    Модель подписчиков
    """
    subscribers: list[SubscriptionDTO]

    class Config:
        frozen = True
        arbitrary_types_allowed = True
