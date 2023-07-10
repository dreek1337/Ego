from pydantic import (
    BaseSettings,
    Field,
)


class APIConfig(BaseSettings):
    """
    Настройки для ювикорна
    """

    host: str = Field(..., env="SITE_HOST")
    port: int = Field(..., env="SITE_PORT")
    loop: str = Field("asyncio")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "users_microservice"
