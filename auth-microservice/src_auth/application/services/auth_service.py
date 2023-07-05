from fastapi_jwt_auth import AuthJWT  # type: ignore
from src_auth.application import use_cases
from src_auth.application.auth_uow import AuthUoW
from src_auth.common import AccessTokenManager, PasswordManager, Service
from src_auth.config.schemas import token_models as tm, user_models as um


class AuthService(Service):
    """
    Сервис для работы с use case
    """

    def __init__(
        self,
        *,
        uow: AuthUoW,
        token_manager: AccessTokenManager,
        password_manager: PasswordManager,
    ) -> None:
        self._uow = uow
        self._token_manager = token_manager
        self._password_manager = password_manager

    async def login_user(
        self, *, data: um.LoginSchema, authorize: AuthJWT
    ) -> tm.TokensData:
        """
        Проверка данных пользователя и выдача токенов
        """
        return await use_cases.UserLoginUseCase(
            uow=self._uow,
            token_manager=self._token_manager,
            password_manager=self._password_manager,
        )(data=data, authorize=authorize)

    async def verify_token(self, authorize: AuthJWT) -> int:
        """
        Проверка токена и выдача payload
        """
        return await use_cases.VerifyAccessTokenUseCase(
            token_manager=self._token_manager
        )(authorize=authorize)

    async def refresh_token(self, authorize: AuthJWT) -> tm.AccessToken:
        """
        Обновление и выдача jwt
        """
        return await use_cases.RefreshAccessTokenUseCase(
            token_manager=self._token_manager
        )(authorize=authorize)

    async def registration_user(
        self, *, authorize: AuthJWT, data: um.CreateUserData
    ) -> tm.TokensData:
        """
        Регистрация пользователя
        """
        return await use_cases.RegistrationUserUseCase(
            uow=self._uow,
            token_manager=self._token_manager,
            password_manager=self._password_manager,
        )(data=data, authorize=authorize)

    async def update_user_data(
        self, *, authorize: AuthJWT, data: um.UpdateUserData
    ) -> um.UsernameData:
        """
        Обнавление данных пользователя
        """
        return await use_cases.UpdateUserUseCase(
            uow=self._uow,
            token_manager=self._token_manager,
            password_manager=self._password_manager,
        )(data=data, authorize=authorize)
