from passlib.context import CryptContext  # type: ignore


class PasswordManagerBase:
    def __init__(self, pwd_context: CryptContext) -> None:
        self._pwd_context = pwd_context
