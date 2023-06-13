from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.config import (
    jwt_config,
    JWTSettings
)


@AuthJWT.load_config
def get_config() -> JWTSettings:
    """
    Разобратсья как рабоатет и переделать в класс все что ниже
    """
    return jwt_config
