from pydantic import Field

from src.application.common import DTO


class SubscriptionDTO(DTO):
    """
    Модель подписок/подписчиков
    """
    subscriber_id: int = Field(..., description='Айди подпичсика')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    avatar: bytes | None = Field(None, description='Аватар пользователя')

    class Config:
        frozen = True
