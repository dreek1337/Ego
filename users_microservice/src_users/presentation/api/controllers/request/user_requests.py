from datetime import date

from pydantic import (
    BaseModel,
    Field,
)
from src_users.domain.common import (
    Empty,
    GenderValue,
)


class CreateUserRequest(BaseModel):
    """
    Модель для создания пользователя
    """

    first_name: str = Field(..., description="Имя пользователя")
    last_name: str = Field(..., description="Фамилия пользователя")
    gender: GenderValue = Field(..., description="Пол пользователя")
    birthday: date = Field(..., description="Дата рождения")


class GetUserRequest(BaseModel):
    """
    Модель для получения пользователя
    """

    user_id: int = Field(..., description="Айди нужного пользователя")


class UpdateUserRequest(BaseModel):
    """
    Модель для обнавления данных
    """

    first_name: str | Empty = Field(Empty.UNSET, description="Имя")
    last_name: str | Empty = Field(Empty.UNSET, description="Фамилия")
    gender: GenderValue | Empty = Field(Empty.UNSET, description="Пол")
    birthday: date | Empty = Field(Empty.UNSET, description="Дата")
