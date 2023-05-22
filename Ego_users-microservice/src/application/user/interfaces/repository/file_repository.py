from abc import (
    ABC,
    abstractmethod
)
from uuid import UUID

from src.domain import FileEntity


class FileRepo(ABC):
    """
    Репозиторий файла
    """
    @abstractmethod
    async def get_file_by_id(self, file_id: UUID) -> FileEntity:
        """Получение файла с помощью id"""

    @abstractmethod
    async def save_file(self, file: FileEntity) -> None:
        """Сохранение файла"""

    @abstractmethod
    async def delete_file(self, file: FileEntity) -> None:
        """Удаление файла"""
