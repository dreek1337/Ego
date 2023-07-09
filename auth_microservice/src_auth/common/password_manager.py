from abc import (
    ABC,
    abstractmethod,
)


class PasswordManager(ABC):
    """
    Абстрактный класс для работы с паролем
    """

    @staticmethod
    @abstractmethod
    def generate_salt() -> str:
        """Возвращает соль для пароля"""

    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Метод проверящюий соответствие пароля"""

    @abstractmethod
    def get_password_hash(self, password: str) -> str:
        """Метод создающий хэш пароля"""
