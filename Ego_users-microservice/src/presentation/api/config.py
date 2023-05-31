from pydantic import (
    Field,
    BaseSettings
)


class APIConfig(BaseSettings):
    """
    Настройки для ювикорна
    """
    host: str = Field(..., env="SITE_HOST")
    port: int = Field(..., env="SITE_PORT")
    loop: str = Field("asyncio")
    log_level: str = Field("info", env="SITE_LOG_LEVEL")
    reload_delay: float = Field(0.25, env="SITE_RELOAD_DELAY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
