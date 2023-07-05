from pydantic import Field
from src.application.common import DTO


class SubscriptionDTO(DTO):
    """
    Модель подписок/подписчиков
    """

    user_id: int = Field(..., description="Айди подпичсика")
    first_name: str = Field(..., description="Имя пользователя")
    last_name: str = Field(..., description="Фамилия пользователя")
    avatar: str | None = Field(None, description="Аватар пользователя")
    deleted: bool = Field(False, description="Показывает удален ли пользователь")

    class Config:
        frozen = True
