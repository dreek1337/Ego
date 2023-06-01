from src.application.user.use_cases import (
    GetUserData,
    CreateUserData
)


class CreateUserRequest(CreateUserData):
    """Форма для создания пользователя"""


class GetUserRequest(GetUserData):
    """Форма для получения пользователя"""
