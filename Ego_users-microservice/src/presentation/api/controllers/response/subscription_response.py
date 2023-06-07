from src.application import SubscribeActionDTO


class SubscribeResponse(SubscribeActionDTO):
    """Модель ответа оформления подписки"""


class UnsubscribeResponse(SubscribeActionDTO):
    """Модель ответа отписки"""
