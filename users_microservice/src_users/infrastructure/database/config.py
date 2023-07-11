import os

from pydantic import (
    BaseSettings,
    Field,
)

env_file = ".env"
cwd_path = os.getcwd()

if os.path.basename(cwd_path) != "users_microservice":
    env_file = os.path.join(cwd_path, "users_microservice", ".env")


class BaseConfigSettings(BaseSettings):
    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"


class DatabaseConfig(BaseConfigSettings):
    """
    Валидация .env для подключения к базе данных
    """

    db_password: str = Field(..., env="DATABASE_PASSWORD")
    db_user: str = Field(..., env="DATABASE_USER")
    db_name: str = Field(..., env="DATABASE_DB")
    db_host: str = Field(..., env="DATABASE_HOST")
    db_port: int = Field(..., env="DATABASE_PORT")

    @property
    def db_connection_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class EngineConfig(BaseConfigSettings):
    url: str = DatabaseConfig().db_connection_url  # type: ignore
    echo: bool = Field(..., env="ORM_ECHO_SETTINGS")
    future: bool = Field(..., env="ORM_FUTURE_SETTINGS")
    pool_size: int = Field(..., env="ORM_POOL_SIZE_SETTINGS")
