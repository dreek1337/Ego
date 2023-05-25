from datetime import date

from pydantic import Field

from src.application.common import DTO


class CreatedUserDTO(DTO):
    """
    Модель пользователя
    """
    user_id: int = Field(..., description='Айди профиля')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    gender: str = Field(..., description='Пол пользователя')
    birthday: date = Field(..., description='День рождения пользователя')

    class Config:
        frozen = True
