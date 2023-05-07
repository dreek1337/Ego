from pydantic import BaseModel, Field, UUID4


class File(BaseModel):
    id: int = Field(..., 'Идентификатор файла')
    file_uuid: UUID4 = Field(..., 'Имя файла в S3')
    size: int = Field(..., 'Размер файла')
    type: str = Field(..., 'Тип файла')
