from fastapi_jwt_auth import AuthJWT  # type: ignore
from src_auth.config import JWTSettings, jwt_config


def create_jwt_auth_factory(authorize: AuthJWT) -> AuthJWT:
    """
    Функция для создания класса, работающего с jwt
    """

    @authorize.load_config
    def get_jwt_auth() -> JWTSettings:
        return jwt_config  # type: ignore

    return authorize
