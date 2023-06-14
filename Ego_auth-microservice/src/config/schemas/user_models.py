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
    salt: str = Field(..., description='Соль для пароля')
    user_email: EmailStr = Field(..., description='Почта пользователя')


class CreateUserData(LoginSchema):
    """
    Схема для создания пользователя
    """
    user_email: str = Field(..., description='Почта пользователя')


class UserSaveDataInDB(CreateUserData):
    """
    Данные с солью для базы данных
    """
    salt: str = Field(..., description='Соль для пароля')


class UpdateUserData(BaseDataModel):
    """
    Данные для обнавления пароля и почты
    """
    password: str | Empty = Field(Empty.UNSET.value)
    user_email: EmailStr | Empty = Field(Empty.UNSET.value)
