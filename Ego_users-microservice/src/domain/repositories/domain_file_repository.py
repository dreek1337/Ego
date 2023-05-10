from abc import (
    ABC,
    abstractmethod
)
from typing import Any

from pydantic import UUID4

from src.domain.models import (
    FileInfo,
    FileContent
)


class FileRepository(ABC):
    @abstractmethod
    def get_file(self, file_uuid: UUID4) -> FileInfo | FileContent:
        """Получаем данные файла"""

    @abstractmethod
    def save_file(self, save_object: Any) -> bool:
        """Сохраняем данные/файл"""

    @abstractmethod
    def update_file(self, update_object: Any) -> bool:
        """Обновляем данные файла"""

    @abstractmethod
    def delete_file(self, file_uuid: UUID4) -> bool:
        """Удаление файла"""
