from pydantic import (
    Field,
    EmailStr
)

from src.config.schemas.base import BaseDataModel


class UserModel(BaseDataModel):
    """
    Схема плученных данных пользователя
    """
    user_id: int = Field(..., description='Айди пользователя')
    username: str = Field(..., description='Никнейм пользователя')
    password: str = Field(..., description='Пароль пользователя')
    user_email: EmailStr = Field(..., description='Почта пользователя')
    deleted: bool = Field(..., description='Статус удаления пользователя')
