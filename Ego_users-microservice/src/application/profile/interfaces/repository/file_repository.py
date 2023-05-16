from abc import (
    ABC,
    abstractmethod
)

from src.domain import FileEntity


class FileRepo(ABC):
    """
    Репозиторий профиля
    """
    @abstractmethod
    async def get_file_by_id(self, file_id: int) -> FileEntity:
        """Получение файла с помощью id"""

    @abstractmethod
    async def update_file(self, file: FileEntity) -> None:
        """Обновление данных файла"""

    @abstractmethod
    async def save_file(self, file: FileEntity) -> None:
        """Сохранение файла"""

    @abstractmethod
    async def delete_file(self, file: FileEntity) -> None:
        """Удаление файла"""
