from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.common import (
    AccessTokenManager,
    UseCase
)


class VerifyAccessTokenUseCase(UseCase):
    """
    Обнавление jwt токена
    """
    def __init__(self, token_manager: AccessTokenManager) -> None:
        self._token_manager = token_manager

    async def __call__(self, authorize: AuthJWT) -> int:
        access_token_subject = self._token_manager.verify_access_token(
            authorize=authorize
        )

        return access_token_subject
