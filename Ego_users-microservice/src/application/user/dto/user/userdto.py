from datetime import date

from pydantic import Field

from src.application.common import DTO
from src.application.user.dto.avatar import AvatarDTO
from src.application.user.dto.subscription import (
    SubscribersDTO,
    SubscriptionsDTO
)


class UserDTO(DTO):
    """
    Модель пользователя
    """
    user_id: int = Field(..., description='Айди профиля')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    gender: str = Field(..., description='Пол пользователя')
    birthday: date = Field(..., description='День рождения пользователя')
    avatar: AvatarDTO | None = Field(None, description='Аватарка пользователя')
    subscriptions: SubscribersDTO | None = Field(..., description='Кол-во подписок')
    subscribers: SubscriptionsDTO | None = Field(..., description='Кол-во подписчиков')
    count_of_subscriptions: int = Field(..., description='Кол-во подписок')
    count_of_subscribers: int = Field(..., description='Кол-во подписчиков')
    deleted: bool = Field(False, description='Пользователь удален/неудален')

    class Config:
        frozen = True
        arbitrary_types_allowed = True
