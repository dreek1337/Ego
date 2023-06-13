from src.common import (
    TokenMaker,
    BaseUseCase
)
from src.config import AccessToken


class UserLoginUseCase(BaseUseCase):
    def __init__(self, token_maker: TokenMaker):
        self._token_maker = token_maker

    async def __call__(self) -> AccessToken:
        new_access_token = self._token_maker.refresh_access_token()

        return new_access_token
