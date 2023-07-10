from pydantic import BaseSettings


class BaseConfigSettings(BaseSettings):
    class Config:
        env_prefix = "auth_microservice"
        env_file = ".env"
        env_file_encoding = "utf-8"
