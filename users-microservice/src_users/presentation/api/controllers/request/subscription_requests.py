from src_users.application.user.use_cases import (
    GetSubscribersData,
    GetSubscriptionsData,
    SubscribeData,
    UnsubscribeData,
)


class SubscribeRequest(SubscribeData):
    """Модель для оформления подписки"""


class UnubscribeRequest(UnsubscribeData):
    """Модель для отписки"""


class GetSubscriptionsRequest(GetSubscriptionsData):
    """Модель для получения подписок"""


class GetSubscribersRequest(GetSubscribersData):
    """Модель для получения подписчиков"""
