from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.config import JWTSettings


@AuthJWT.load_config
def get_jwt_auth(config: JWTSettings) -> JWTSettings:
    """
    Разобратсья как рабоатет и переделать в класс все что ниже
    """
    return config
