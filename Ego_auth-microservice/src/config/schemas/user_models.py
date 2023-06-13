from datetime import date

from pydantic import (
    Field,
    EmailStr
)

from src.common import Empty
from src.config import BaseDataModel


class UserIdData(BaseDataModel):
    """
    Схема для получения пользователя по айди
    """
    user_id: int = Field(..., description='Айди пользователя')


class UsernameData(BaseDataModel):
    """
    Логин пользователя
    """
    username: str = Field(..., description='Никнейм пользователя')


class LoginSchema(UsernameData):
    """
    Данные для логина
    """
    password: str = Field(..., description='Пароль пользователя')


class UserModel(UserIdData, LoginSchema):
    """
    Схема плученных данных пользователя
    """
    user_email: EmailStr = Field(..., description='Почта пользователя')
    deleted: bool = Field(..., description='Статус удаления пользователя')


class CreateUserData(LoginSchema):
    """
    Схема для создания пользователя
    """
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    gender: str = Field(..., description='Пол пользователя')
    birthday: date = Field(..., description='Дата рождения пользователя')
    user_email: str = Field(..., description='Почта пользователя')


class UpdateUserData(BaseDataModel):
    """
    Данные для обнавления пароля и почты
    """
    password: str | Empty = Field(Empty.UNSET.value)
    user_email: str | Empty = Field(Empty.UNSET.value)
    deleted: bool | Empty = Field(Empty.UNSET.value)
