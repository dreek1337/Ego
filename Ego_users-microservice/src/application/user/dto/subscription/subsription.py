from pydantic import Field

from src.application.common import DTO


class BaseSubscription(DTO):
    """
    Модель подписок/подписчиков
    """
    user_id: int = Field(..., description='Айди пользователя')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')

    class Config:
        frozen = True


class Subscription(BaseSubscription):
    """Создание модели подписки"""


class Subscriber(BaseSubscription):
    """Создание модели подписчика"""
