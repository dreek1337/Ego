from pydantic import Field

from src.config.schemas.base import BaseDataModel


class AccessToken(BaseDataModel):
    """
    Модель токена
    """
    access_token: str = Field(..., description='Jwt для авторизации')


class TokensData(AccessToken):
    """
    Модель формирования токинов
    """
    refresh_token: str = Field(..., description='Рефреш токен для обнавления jwt')
    access_token_expires: int = Field(..., description='Время, сколько активен jwt')
