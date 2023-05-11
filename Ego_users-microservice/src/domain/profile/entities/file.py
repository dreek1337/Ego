from dataclasses import dataclass
from typing import Self
from uuid import UUID

from src.domain.common import Empty
from src.domain.profile.value_objects import (
    FileType,
    FileContent
)


@dataclass
class File:
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
        file = File(
            file_id=file_id,
            file_type=file_type,
            file_content=file_content
        )

        return file

    def update_file(
            self,
            *,
            file_type: FileType | Empty = Empty.UNSET,
            file_content: FileContent | Empty = Empty.UNSET
    ) -> None:
        """
        Обнавление файла
        """
        if file_type is not Empty.UNSET:
            self.file_type = file_type
        if file_content is not Empty.UNSET:
            self.file_content = file_content
