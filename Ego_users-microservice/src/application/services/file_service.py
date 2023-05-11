from typing import Any

from pydantic import UUID4

from src.domain.common import (
    FileInfo,
    FileContent
)
from src.application.repositories import FileRepository


class FileService:
    def __init__(self, file_repository: FileRepository) -> None:
        self.file_repository = file_repository

    def get_file_data(self, file_uuid: UUID4) -> FileContent | FileInfo:
        """
        Получение файла
        """
        return self.file_repository.get_file(file_uuid=file_uuid)

    def save_file_data(self, save_object: Any) -> bool:
        """
        Сохранение фотографии
        """
        return self.file_repository.save_file(save_object=save_object)

    def update_file(self, update_object: Any) -> bool:
        """
        Обнавление данных фото
        """
        return self.file_repository.update_file(update_object=update_object)

    def delete_file(self, file_uuid: UUID4) -> bool:
        """
        Удаление файла
        """
        return self.file_repository.delete_file(file_uuid=file_uuid)
