from fastapi_jwt_auth import AuthJWT  # type: ignore
from src_auth.application.auth_uow import AuthUoW
from src_auth.common import (
    AccessTokenManager,
    Empty,
    PasswordManager,
    UseCase,
)
from src_auth.config.schemas.user_models import (
    UpdateUserData,
    UsernameData,
)


class UpdateUserUseCase(UseCase):
    """
    Обнавление данных пользователя для входа
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

    async def __call__(
        self, *, authorize: AuthJWT, data: UpdateUserData
    ) -> UsernameData:
        user_id = self._token_manager.verify_access_token(authorize=authorize)

        user = await self._uow.user_repo.get_user_by_id(user_id=user_id)

        if data.password != Empty.UNSET:
            hashed_password = self._password_manager.get_password_hash(
                password=data.password + user.salt
            )

            user.password = hashed_password

        if data.user_email != Empty.UNSET:
            user.user_email = data.user_email  # type: ignore

        await self._uow.user_repo.update_user(data=user)
        await self._uow.commit()

        return UsernameData(username=user.username)
