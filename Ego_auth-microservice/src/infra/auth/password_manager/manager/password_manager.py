import bcrypt

from src.common import PasswordManager
from src.infra.auth.password_manager.manager.base import PasswordManagerBase


class PasswordManagerImpl(PasswordManagerBase, PasswordManager):
    @staticmethod
    def generate_salt() -> str:
        return bcrypt.gensalt().decode()

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self._pwd_context.hash(password)
