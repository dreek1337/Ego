from datetime import datetime

from pydantic import Field

from src.application.common import DTO
from src.application.profile.dto import File
from src.application.profile.dto import Post


class Profile(DTO):
    """
    Модель профиля
    """
    profile_id: int = Field(..., description='Айди профиля')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    gender: str = Field(..., description='Пол пользователя')
    birthday: datetime = Field(..., description='День рождения пользователя')
    photo: File | None = Field(None, description='Аватарка пользователя')
    posts: list[Post] | None = Field(None, description='Посты пользователя')
    subscriptions: int = Field(..., description='Колличество подписок')
    subscribers: int = Field(..., description='Колличество подписчиков')
    deleted: bool = Field(False, description='Указывает, что пользователь удален/неудален')

    class Config:
        frozen = True
