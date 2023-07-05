from datetime import timedelta

from pydantic import Field
from src_auth.config.settings.base import BaseConfigSettings


class JWTSettings(BaseConfigSettings):
    authjwt_secret_key: str = Field(..., env="AUTH_SECRET_KEY")
    authjwt_access_token_expires: timedelta = timedelta(minutes=60)
