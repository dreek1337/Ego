from pydantic import (
    BaseModel,
    Field,
)
from src_users.application.user.use_cases import (
    GetSubscribersData,
    GetSubscriptionsData,
)


class SubscribeRequest(BaseModel):
    """
    Модель для оформления подписки
    """

    subscription_id: int = Field(..., description="Айди на кого подписка")


class UnsubscribeRequest(BaseModel):
    """
    Модель для отписки
    """

    subscription_id: int = Field(..., description="Айди от кого отписка")


class GetSubscriptionsRequest(GetSubscriptionsData):
    """
    Модель для получения подписок
    """


class GetSubscribersRequest(GetSubscribersData):
    """Модель для получения подписчиков"""
