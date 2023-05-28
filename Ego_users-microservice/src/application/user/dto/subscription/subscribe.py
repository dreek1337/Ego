from src.application.common import DTO


class SubscribeDTO(DTO):
    """
    Модель оформления подписчки
    """
    subscriber_id: int
    subscription_id: int

    class Config:
        frozen = True
