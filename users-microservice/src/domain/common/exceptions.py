class AbstractBaseException(Exception):
    """Базовый класс ошибки"""
    @property
    def message(self) -> str:
        """
        Сообщение об ошибке
        """
        return 'An application error occurred'
