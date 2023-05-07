from abc import ABC, abstractmethod


class FileRepository(ABC):
    @abstractmethod
    def save_file(self) -> None:
        """Сохраняем данные/файл"""

    @abstractmethod
    def get_file(self) -> File | bytes:
        """Получаем данные файла"""

    @abstractmethod
    def update_file(self) -> None:
        """Обновляем данные файла"""
