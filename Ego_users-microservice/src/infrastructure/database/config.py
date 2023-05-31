from pydantic import (
    Field,
    BaseModel,
    BaseSettings
)


class DatabaseConfig(BaseSettings):
    """
    Валидация .env для подключения к базе данных
    """
    db_password: str = Field(..., env='DATABASE_PASSWORD')
    db_user: str = Field(..., env='DATABASE_USER')
    db_name: str = Field(..., env='DATABASE_DB')
    db_host: str = Field(..., env='DATABASE_HOST')
    db_port: int = Field(..., env='DATABASE_PORT')
    echo: bool = Field(..., env='ORM_ECHO_SETTINGS')

    @property
    def db_connection_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class EngineConfig(BaseModel):
    url: str = DatabaseConfig().db_connection_url  # type: ignore
    echo_pool: bool = DatabaseConfig().echo  # type: ignore
    future: bool = True
    pool_size: int = 50
