from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.common import UseCase
from src.config.schemas.token_models import AccessToken
from src.common import AccessTokenManager


class RefreshAccessTokenUseCase(UseCase):
    """
    Обнавление jwt токена
    """
    def __init__(self, token_manager: AccessTokenManager) -> None:
        self._token_manager = token_manager

    async def __call__(self, authorize: AuthJWT) -> AccessToken:
        new_access_token = self._token_manager.refresh_access_token(
            authorize=authorize
        )

        return new_access_token
