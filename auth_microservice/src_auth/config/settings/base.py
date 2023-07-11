import os

from pydantic import BaseSettings

env_file = ".env"
cwd_path = os.getcwd()

if os.path.basename(cwd_path) != "auth_microservice":
    env_file = os.path.join(cwd_path, "auth_microservice", ".env")


class BaseConfigSettings(BaseSettings):
    class Config:
        env_file = env_file
        env_file_encoding = "utf-8"
