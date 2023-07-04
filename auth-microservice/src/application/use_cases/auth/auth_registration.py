from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.application.auth_uow import AuthUoW
from src.config.schemas.token_models import TokensData
from src.common import (
    UseCase,
    PasswordManager,
    AccessTokenManager
)
from src.config.schemas.user_models import (
    UserIdData,
    CreateUserData,
    UserSaveDataInDB
)


class RegistrationUserUseCase(UseCase):
    """
    Регистрация пользователя
    """
    def __init__(
            self,
            *,
            uow: AuthUoW,
            token_manager: AccessTokenManager,
            password_manager: PasswordManager
    ) -> None:
        self._uow = uow
        self._token_manager = token_manager
        self._password_manager = password_manager

    async def __call__(
            self,
            *,
            authorize: AuthJWT,
            data: CreateUserData) -> TokensData:
        salt = self._password_manager.generate_salt()
        hashed_password = self._password_manager.get_password_hash(
            password=data.password + salt
        )

        create_user_data = UserSaveDataInDB(
            username=data.username,
            password=hashed_password,
            salt=salt,
            user_email=data.user_email
        )

        await self._uow.user_repo.create_user(data=create_user_data)
        await self._uow.commit()

        user = await self._uow.user_repo.get_user_by_username(
            username=data.username
        )

        tokens = self._token_manager.create_tokens(
            authorize=authorize,
            subject=UserIdData(user_id=user.user_id)
        )

        return tokens
