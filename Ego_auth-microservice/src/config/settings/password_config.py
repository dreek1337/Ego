from pydantic import Field

from src.config.settings.base import BaseConfigSettings


class PasswordConfig(BaseConfigSettings):
    schemes: list = Field(["bcrypt"])
    deprecated: str = Field("auto")
