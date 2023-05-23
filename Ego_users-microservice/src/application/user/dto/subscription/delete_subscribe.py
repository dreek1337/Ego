from src.application.common import DTO


class DeleteSubscriptionDTO(DTO):
    """Модель отписки"""
    user_id: int
    subscription_id: int

    class Config:
        frozen = True
