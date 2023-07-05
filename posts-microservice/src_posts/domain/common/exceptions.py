from abc import ABC


class AbstractBaseException(Exception, ABC):
    """
    Вазовый класс ошибок приложения
    """

    @property
    def message(self) -> str:
        return "Application exception"
