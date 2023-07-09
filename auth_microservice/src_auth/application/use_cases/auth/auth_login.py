from fastapi_jwt_auth import AuthJWT  # type: ignore
from src_auth.application.auth_uow import AuthUoW
from src_auth.application.exceptions import UserDataIsNotCorrect
from src_auth.common import (
    AccessTokenManager,
    PasswordManager,
    UseCase,
)
from src_auth.config.schemas.token_models import TokensData
from src_auth.config.schemas.user_models import (
    LoginSchema,
    UserIdData,
)


class UserLoginUseCase(UseCase):
    """
    Логика входа в сервис
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

    async def __call__(self, *, data: LoginSchema, authorize: AuthJWT) -> TokensData:
        user = await self._uow.user_repo.get_user_by_username(username=data.username)

        check_on_correct_password = self._password_manager.verify_password(
            plain_password=data.password + user.salt, hashed_password=user.password
        )

        if not check_on_correct_password:
            raise UserDataIsNotCorrect()

        tokens = self._token_manager.create_tokens(
            authorize=authorize, subject=UserIdData(user_id=user.user_id)
        )

        return tokens
