from src.config.schemas.user_models import UsernameData
from src.config.schemas.token_models import TokensData, AccessToken


class RegistrationResponse(UsernameData):
    """Ответ сервера на регистрацию"""


class TokensResponse(TokensData):
    """Выдача токенов"""


class RefreshTokenResponse(AccessToken):
    """Модель обнавленного ткоена"""
