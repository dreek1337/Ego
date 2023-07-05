from src_auth.config.schemas.user_models import CreateUserData, LoginSchema


class RegistrationRequest(CreateUserData):
    """Модель регистрации пользоватлея"""


class LoginRequest(LoginSchema):
    """Модель входа в систему"""
