from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.config import (
    UserIdData,
    jwt_config,
    TokensData,
    JWTSettings,
    AccessToken
)


@AuthJWT.load_config
def get_config() -> JWTSettings:
    """
    Разобратсья как рабоатет и переделать в класс все что ниже
    """
    return jwt_config


def creat_tokens(
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
        access_token_expires=jwt_config.authjwt_access_token_expires.seconds
    )


def refresh_access_token(authorize: AuthJWT) -> AccessToken:
    """
    Обновление jwt
    """
    authorize.jwt_refresh_token_required()

    user_id = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=user_id)

    return AccessToken(access_token=new_access_token)
