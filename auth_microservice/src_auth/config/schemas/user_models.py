from pydantic import (
    EmailStr,
    Field,
    validator,
)
from src_auth.common import Empty
from src_auth.config.schemas.base import BaseDataModel


class UserIdData(BaseDataModel):
    """
    Схема для получения пользователя по айди
    """

    user_id: int = Field(..., description="Айди пользователя")


class UsernameData(BaseDataModel):
    """
    Логин пользователя
    """

    username: str = Field(..., description="Никнейм пользователя")


class LoginSchema(UsernameData):
    """
    Данные для логина
    """

    password: str = Field(..., description="Пароль пользователя")


class UserModel(UserIdData, LoginSchema):
    """
    Схема плученных данных пользователя
    """

    salt: str = Field(..., description="Соль для пароля")
    user_email: EmailStr = Field(..., description="Почта пользователя")


class CreateUserData(LoginSchema):
    """
    Схема для создания пользователя
    """

    user_email: EmailStr = Field(..., description="Почта пользователя")

    @validator("password")
    def check_password(cls, password):
        if len(password) > 32:
            raise ValueError("string is too long")
        if len(password) < 8:
            raise ValueError("string is too small")

        return password


class UserSaveDataInDB(LoginSchema):
    """
    Данные с солью для базы данных
    """

    salt: str = Field(..., description="Соль для пароля")
    user_email: EmailStr = Field(..., description="Почта пользователя")


class UpdateUserData(BaseDataModel):
    """
    Данные для обнавления пароля и почты
    """

    password: str | Empty = Field(Empty.UNSET.value)
    user_email: EmailStr | Empty = Field(Empty.UNSET.value)

    @validator("password")
    def check_password(cls, password):
        if password == Empty.UNSET.value:
            return password

        if len(password) > 32:
            raise ValueError("string is too long")
        if len(password) < 8:
            raise ValueError("string is too small")

        return password
