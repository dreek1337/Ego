from pydantic import Field
from src.config.settings.base import BaseConfigSettings


class APIConfig(BaseConfigSettings):
    """
    Настройки для ювикорна
    """
    host: str = Field(..., env="SITE_HOST")
    port: int = Field(..., env="SITE_PORT")
    loop: str = Field("asyncio")
