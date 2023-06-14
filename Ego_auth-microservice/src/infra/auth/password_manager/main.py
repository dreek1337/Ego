from passlib.context import CryptContext  # type: ignore

from src.config import PasswordConfig


def create_pwd_context(config: PasswordConfig) -> CryptContext:
    pwd_context = CryptContext(**config.dict())

    return pwd_context
