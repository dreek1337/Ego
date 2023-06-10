from src.application.user.use_cases import (
    SubscribeData,
    UnsubscribeData,
    GetSubscribersData,
    GetSubscriptionsData
)


class SubscribeRequest(SubscribeData):
    """Модель для оформления подписки"""


class UnubscribeRequest(UnsubscribeData):
    """Модель для отписки"""


class GetSubscriptionsRequest(GetSubscriptionsData):
    """Модель для получения подписок"""


class GetSubscribersRequest(GetSubscribersData):
    """Модель для получения подписчиков"""
