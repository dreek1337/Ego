from pydantic import Field
from src_auth.config.settings.base import BaseConfigSettings


class APIConfig(BaseConfigSettings):
    """
    Настройки для ювикорна
    """

    host: str = Field("host", env="SITE_HOST")
    port: int = Field(7654, env="SITE_PORT")
    loop: str = Field("asyncio")
