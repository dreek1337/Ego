import os

from pydantic import (
    BaseSettings,
    Field,
)

env_file = ".env"
cwd_path = os.getcwd()

if os.path.basename(cwd_path) != "posts_microservice":
    env_file = os.path.join(cwd_path, "posts_microservice", ".env")


class APIConfig(BaseSettings):
    """
    Настройки для ювикорна
    """

    host: str = Field(..., env="SITE_HOST")
    port: int = Field(..., env="SITE_PORT")
    loop: str = Field("asyncio")

    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"
