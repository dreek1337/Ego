from pydantic import BaseSettings


class BaseConfigSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
