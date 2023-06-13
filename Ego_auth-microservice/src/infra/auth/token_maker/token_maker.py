from src.common import TokenMaker
from src.infra.auth.token_maker.base import TokenMakerBase
from src.config import (
    UserIdData,
    jwt_config,
    TokensData,
    AccessToken
)


class TokenMakerImpl(TokenMakerBase, TokenMaker):
    """
    Реализация класса для работы с токеном
    """
    def create_tokens(self, subject: UserIdData) -> TokensData:
        """
        Создание рефреш и ацесс токена
        """
        access_token = self._authorize.create_access_token(subject=subject.user_id)
        refresh_token = self._authorize.create_refresh_token(subject=subject.user_id)

        return TokensData(
            access_token=access_token,
            refresh_token=refresh_token,
            access_token_expires=(
                jwt_config
                .authjwt_access_token_expires
                .seconds
            )  # type: ignore
        )

    def refresh_access_token(self) -> AccessToken:
        """
        Обновление jwt
        """
        self._authorize.jwt_refresh_token_required()

        user_id = self._authorize.get_jwt_subject()
        new_access_token = self._authorize.create_access_token(subject=user_id)

        return AccessToken(access_token=new_access_token)
