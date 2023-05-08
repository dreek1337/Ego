from abc import ABC, abstractmethod

from src.domain.models import File


class FileRepository(ABC):
    @abstractmethod
    def get_file(self) -> File | bytes:
        """Получаем данные файла"""

    @abstractmethod
    def save_file(self) -> None:
        """Сохраняем данные/файл"""

    @abstractmethod
    def update_file(self) -> None:
        """Обновляем данные файла"""

    @abstractmethod
    def delete_file(self) -> None:
        """Удаление файла"""
