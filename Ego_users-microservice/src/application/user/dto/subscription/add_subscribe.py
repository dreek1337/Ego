from src.application.common import DTO


class AddSubscriptionDTO(DTO):
    """Модель оформления подписчки"""
    user_id: int
    subscription_id: int

    class Config:
        frozen = True
