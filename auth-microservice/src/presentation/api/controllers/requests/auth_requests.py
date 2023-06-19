from src.config.schemas.user_models import (
    LoginSchema,
    CreateUserData
)


class RegistrationRequest(CreateUserData):
    """Модель регистрации пользоватлея"""


class LoginRequest(LoginSchema):
    """Модель входа в систему"""
