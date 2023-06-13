from abc import (
    ABC,
    abstractmethod
)


class TokenMaker(ABC):
    """
    Класс для работы с токенами
    """
    @abstractmethod
    def create_tokens(self) -> None:
        pass
