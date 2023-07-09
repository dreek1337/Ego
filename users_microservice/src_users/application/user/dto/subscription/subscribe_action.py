from src_users.application.common import DTO


class SubscribeActionDTO(DTO):
    """
    Модель оформления подписчки и отписки
    """

    subscriber_id: int
    subscription_id: int

    class Config:
        frozen = True
