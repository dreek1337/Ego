from src.application import SubscribeActionDTO, SubscribersDTO, SubscriptionsDTO


class SubscribeResponse(SubscribeActionDTO):
    """Модель ответа оформления подписки"""


class UnsubscribeResponse(SubscribeActionDTO):
    """Модель ответа отписки"""


class SubscriptionsResponse(SubscriptionsDTO):
    """Модель ответа получения подписок"""


class SubscribersResponse(SubscribersDTO):
    """Модель ответа получения подписчиков"""
