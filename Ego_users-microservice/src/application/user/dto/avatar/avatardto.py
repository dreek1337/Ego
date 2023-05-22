from pydantic import (
    Field,
    UUID4
)

from src.application.common import DTO


class AvatarDTO(DTO):
    """
    Информация о файле
    """
    avatar_id: UUID4 = Field(None, description='Айди файла')
    avatar_type: str = Field(None, description='Формат файла')
    avatar_content: bytes = Field(None, description='Байты файла')
    user_id: int = Field(None, description='Айди пользователя, кому предналежит аватар')

    class Config:
        frozen = True
