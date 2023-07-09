from pydantic import Field
from src_auth.config.settings.base import BaseConfigSettings


class PasswordConfig(BaseConfigSettings):
    schemes: list = Field(["bcrypt"])
    deprecated: str = Field("auto")
