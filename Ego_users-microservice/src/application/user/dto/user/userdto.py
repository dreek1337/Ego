from datetime import datetime

from pydantic import Field

from src.application.common import DTO
from src.application.user.dto.avatar.avatardto import AvatarDTO


class UserDTO(DTO):
    """
    Модель пользователя
    """
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    gender: str = Field(..., description='Пол пользователя')
    birthday: datetime = Field(..., description='День рождения пользователя')
    photo: AvatarDTO | None = Field(None, description='Аватарка пользователя')
    subscriptions: int = Field(..., description='Колличество подписок')
    subscribers: int = Field(..., description='Колличество подписчиков')
    deleted: bool = Field(False, description='Указывает, что пользователь удален/неудален')

    class Config:
        frozen = True
        arbitrary_types_allowed = True
