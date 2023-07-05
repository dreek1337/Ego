from pydantic import validator
from src_users.application import (
    CreateUserData,
    DeleteUserData,
    GetUserData,
    UpdateUserData,
)
from src_users.domain.common import Empty


class CreateUserRequest(CreateUserData):
    """Модель для создания пользователя"""

    @validator("gender", pre=True)
    def lower_gender(cls, value: str) -> str:
        return value.lower()


class GetUserRequest(GetUserData):
    """Модель для получения пользователя"""


class UpdateUserRequest(UpdateUserData):
    """Модель для обнавления данных"""

    @validator("gender", pre=True)
    def lower_gender(cls, value: str) -> str:
        if value != Empty.UNSET:
            value = value.lower()

        return value


class DeleteUserRequest(DeleteUserData):
    """Модель для удаления пользователя"""
