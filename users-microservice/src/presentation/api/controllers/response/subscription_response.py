from src.application import (
    SubscribersDTO,
    SubscriptionsDTO,
    SubscribeActionDTO
)


class SubscribeResponse(SubscribeActionDTO):
    """Модель ответа оформления подписки"""


class UnsubscribeResponse(SubscribeActionDTO):
    """Модель ответа отписки"""


class SubscriptionsResponse(SubscriptionsDTO):
    """Модель ответа получения подписок"""


class SubscribersResponse(SubscribersDTO):
    """Модель ответа получения подписчиков"""
