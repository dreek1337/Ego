from abc import (
    ABC,
    abstractmethod
)

from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.config.schemas.user_models import UserIdData
from src.config.schemas.token_models import (
    TokensData,
    AccessToken
)


class AccessTokenManager(ABC):
    """
    Класс для работы с токенами
    """
    @abstractmethod
    def create_tokens(
            self,
            *,
            authorize: AuthJWT,
            subject: UserIdData
    ) -> TokensData:
        """Создание access и refresh токенов"""

    @abstractmethod
    def refresh_access_token(self, authorize: AuthJWT) -> AccessToken:
        """Обнавление access токена"""

    @abstractmethod
    def verify_access_token(self, authorize: AuthJWT) -> int:
        """Проверка токена"""
