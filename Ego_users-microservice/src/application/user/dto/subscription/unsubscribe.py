from src.application.common import DTO


class UnsubscribeDTO(DTO):
    """
    Модель отписки
    """
    subscriber_id: int
    subscription_id: int

    class Config:
        frozen = True
