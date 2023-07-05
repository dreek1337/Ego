from abc import ABC, abstractmethod


class UnitOfWork(ABC):
    @abstractmethod
    async def commit(self) -> None:
        """Сохранение изменений в бд"""

    @abstractmethod
    async def rollback(self) -> None:
        """Откат изменений в бд"""
