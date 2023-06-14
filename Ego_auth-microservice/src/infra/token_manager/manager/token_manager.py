from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.common import AccessTokenManager

from src.config import (
    UserIdData,
    jwt_config,
    TokensData,
    AccessToken
)


class AccessTokenManagerImpl(AccessTokenManager):
    """
    Реализация класса для работы с токеном
    """
    def create_tokens(
            self,
            *,
            authorize: AuthJWT,
            subject: UserIdData
    ) -> TokensData:
        """
        Создание рефреш и ацесс токена
        """
        access_token = authorize.create_access_token(subject=subject.user_id)
        refresh_token = authorize.create_refresh_token(subject=subject.user_id)

        return TokensData(
            access_token=access_token,
            refresh_token=refresh_token,
            access_token_expires=(
                jwt_config
                .authjwt_access_token_expires
                .seconds
            )  # type: ignore
        )

    def refresh_access_token(self, authorize: AuthJWT) -> AccessToken:
        """
        Обновление jwt
        """
        authorize.jwt_refresh_token_required()

        user_id = authorize.get_jwt_subject()
        new_access_token = authorize.create_access_token(subject=user_id)

        return AccessToken(access_token=new_access_token)

    def verify_access_token(self, authorize: AuthJWT) -> int:
        """
        Проверка токена и возвращение айди пользователя из payload
        """
        authorize.jwt_required()

        user_id = authorize.get_jwt_subject()

        return user_id
