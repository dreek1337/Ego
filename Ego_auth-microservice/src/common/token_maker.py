from abc import (
    ABC,
    abstractmethod
)

from src.config import (
    UserIdData,
    TokensData,
    AccessToken
)


class TokenMaker(ABC):
    """
    Класс для работы с токенами
    """
    @abstractmethod
    def create_tokens(self, subject: UserIdData) -> TokensData:
        """Создание access и refresh токенов"""

    @abstractmethod
    def refresh_access_token(self) -> AccessToken:
        """Обнавление access токена"""
