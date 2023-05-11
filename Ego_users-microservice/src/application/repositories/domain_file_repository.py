from abc import (
    ABC,
    abstractmethod
)
from typing import Any, Callable

from pydantic import UUID4

from src.domain.common import FileInfo


class FileRepository(ABC):
    def __init__(self, session: Callable) -> None:
        self.session = session

    @abstractmethod
    def get_file(self, file_uuid: UUID4) -> FileInfo:
        """Получаем данные файла"""

    @abstractmethod
    def save_file(self, save_object: FileInfo) -> bool:
        """Сохраняем данные/файл"""

    @abstractmethod
    def update_file(self, update_object: FileInfo) -> bool:
        """Обновляем данные файла"""

    @abstractmethod
    def delete_file(self, file_uuid: UUID4) -> bool:
        """Удаление файла"""
