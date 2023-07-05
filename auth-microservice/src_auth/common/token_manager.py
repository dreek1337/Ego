from abc import ABC, abstractmethod
from typing import Any, TypeVar

from src_auth.config.schemas.token_models import AccessToken, TokensData
from src_auth.config.schemas.user_models import UserIdData

AuthSettings = TypeVar("AuthSettings", bound=Any)


class AccessTokenManager(ABC):
    """
    Класс для работы с токенами
    """

    @abstractmethod
    def create_tokens(
        self, *, authorize: AuthSettings, subject: UserIdData
    ) -> TokensData:
        """Создание access и refresh токенов"""

    @abstractmethod
    def refresh_access_token(self, authorize: AuthSettings) -> AccessToken:
        """Обнавление access токена"""

    @abstractmethod
    def verify_access_token(self, authorize: AuthSettings) -> int:
        """Проверка токена"""
