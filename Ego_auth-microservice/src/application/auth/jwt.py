from fastapi_jwt_auth import AuthJWT

from src.config import jwt_config


@AuthJWT.load_config
def get_config():
    return jwt_config
