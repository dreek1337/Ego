from pydantic import (
    Field,
    UUID4
)

from src.application.common import DTO


class File(DTO):
    """
    Информация о файле
    """
    file_id: UUID4 = Field(..., description='Айди файла/имя')
    file_type: str = Field(..., description='Формат файла')
    file_content: bytes | None = Field(None, description='Байты файла')

    class Config:
        frozen = True
