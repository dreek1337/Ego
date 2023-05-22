from typing import Self
from uuid import UUID

from dataclasses import dataclass

from src.domain.user.value_objects import (
    FileType,
    FileContent
)


@dataclass
class FileEntity:
    """
    Информация о файле
    """
    file_id: UUID
    file_type: FileType
    file_content: FileContent

    @classmethod
    def create_file(
            cls,
            *,
            file_id: UUID,
            file_type: FileType,
            file_content: FileContent
    ) -> Self:
        """
        Создание файла
        """
        file = FileEntity(
            file_id=file_id,
            file_type=file_type,
            file_content=file_content
        )

        return file
