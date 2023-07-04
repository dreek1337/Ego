from typing import Any

from fastapi_jwt_auth.exceptions import (  # type: ignore
    JWTDecodeError,  # type: ignore
    RefreshTokenRequired  # type: ignore
)

from src.common import AccessTokenManager
from src.config.schemas.user_models import UserIdData
from src.config.schemas.token_models import (
    TokensData,
    AccessToken
)


class AccessTokenManagerMock(AccessTokenManager):
    """
    Мок для работы с jwt
    """
    def __init__(self) -> None:
        self.jwt_data: dict = dict()

    def create_tokens(self, authorize: Any, subject: UserIdData) -> TokensData:
        """
        Создание access и refresh токенов
        """
        token_data = TokensData(
            access_token=f'some.{subject.user_id}',
            refresh_token='some_refresh',
            access_token_expires=2
        )

        return token_data

    def refresh_access_token(
            self,
            authorize: Any,
    ) -> AccessToken:
        """
        Обнавление access токена
        """
        if self.jwt_data.get("refresh_token") == authorize.ref_token:
            return AccessToken(access_token='new_token')
        raise RefreshTokenRequired(status_code=401, message='Bad access token!')

    def verify_access_token(
            self, authorize: Any,
    ) -> int:
        """Проверка токена"""
        if authorize:
            if self.jwt_data.get("access_token") == authorize.acc_token:
                return int(authorize.acc_token.split('.')[1])
        raise JWTDecodeError(status_code=401, message='Bad access token!')

    def add_jwt_data(
            self,
            *,
            token_data: TokensData,
    ) -> None:
        self.jwt_data = token_data.dict()
