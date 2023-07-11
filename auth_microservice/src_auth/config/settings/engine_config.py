from pydantic import Field
from src_auth.config.settings.base import BaseConfigSettings


class DatabaseConfig(BaseConfigSettings):
    """
    Валидация .env для подключения к базе данных
    """

    db_password: str = Field("pass", env="DATABASE_PASSWORD")
    db_user: str = Field("user", env="DATABASE_USER")
    db_name: str = Field("name", env="DATABASE_DB")
    db_host: str = Field("host", env="DATABASE_HOST")
    db_port: int = Field(5432, env="DATABASE_PORT")

    @property
    def db_connection_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class EngineConfig(BaseConfigSettings):
    url: str = DatabaseConfig().db_connection_url  # type: ignore
    echo: bool = Field(False, env="ORM_ECHO_SETTINGS")
    future: bool = Field(True, env="ORM_FUTURE_SETTINGS")
    pool_size: int = Field(10, env="ORM_POOL_SIZE_SETTINGS")
