from abc import (
    ABC,
    abstractmethod
)


class UnitOfWork(ABC):
    @abstractmethod
    async def commit(self) -> None:
        """Происходит коммит"""

    @abstractmethod
    async def rollback(self) -> None:
        """Происходит ролбэк"""
