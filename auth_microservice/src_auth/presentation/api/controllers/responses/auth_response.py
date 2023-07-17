from pydantic import (
    BaseModel,
    Field,
)
from src_auth.config.schemas.token_models import (
    AccessToken,
    TokensData,
)
from src_auth.config.schemas.user_models import UsernameData


class TokensResponse(TokensData):
    """Выдача токенов"""


class RefreshTokenResponse(AccessToken):
    """Модель обнавленного ткоена"""


class VerifyStatus(BaseModel):
    verify_status: str = Field("Done")


class UpdateLoginUserResponse(UsernameData):
    """Модель ответа об обновлении пользователя"""
