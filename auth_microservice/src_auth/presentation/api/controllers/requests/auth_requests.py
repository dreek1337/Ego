from src_auth.config.schemas.user_models import (
    CreateUserData,
    LoginSchema,
    UpdateUserData,
)


class RegistrationRequest(CreateUserData):
    """Модель регистрации пользоватлея"""


class LoginRequest(LoginSchema):
    """Модель входа в систему"""


class UpdateLoginUserRequest(UpdateUserData):
    """Модель для обнавление данных пользователя"""
