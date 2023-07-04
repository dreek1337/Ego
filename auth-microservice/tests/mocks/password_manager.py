from src.common import PasswordManager


class PasswordManagerMock(PasswordManager):
    """
    Мок для работы с паролем
    """
    @staticmethod
    def generate_salt() -> str:
        """
        Возвращает соль для пароля
        """
        return 'my_salt'

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Метод проверящюий соответствие пароля
        """
        return self.get_password_hash(plain_password) == hashed_password

    def get_password_hash(self, password: str) -> str:
        """
        Метод создающий хэш пароля
        """
        return password + 'hashed_hashed'
