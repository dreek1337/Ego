from src.application.user.use_cases import (
    SubscribeData,
    UnsubscribeData
)


class SubscribeRequest(SubscribeData):
    """Модель для оформления подписки"""


class UnubscribeRequest(UnsubscribeData):
    """Модель для отписки"""
