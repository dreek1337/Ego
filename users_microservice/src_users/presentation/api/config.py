from pydantic import (
    BaseSettings,
    Field,
)


class APIConfig(BaseSettings):
    """
    Настройки для ювикорна
    """

    host: str = Field("host", env="SITE_HOST")
    port: int = Field(9876, env="SITE_PORT")
    loop: str = Field("asyncio")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
