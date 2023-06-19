from src.config.schemas.token_models import (
    TokensData,
    AccessToken
)


class TokensResponse(TokensData):
    """Выдача токенов"""


class RefreshTokenResponse(AccessToken):
    """Модель обнавленного ткоена"""
