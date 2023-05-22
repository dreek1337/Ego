from abc import (
    ABC,
    abstractmethod
)


class AbstractBaseException(Exception, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        """Сообщение об ошибке"""
