from dataclasses import dataclass

from src.domain.models.value_objects import (
    FileUuid,
    FileType,
    FileContent
)


@dataclass
class FileInfo:
    """
    Информация о файле
    """
    file_uuid: FileUuid
    file_type: FileType
    file_content: FileContent
