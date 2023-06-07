from pydantic import (
    Field,
    UUID4
)

from src.application.common import DTO


class AvatarDTO(DTO):
    """
    Информация о файле
    """
    avatar_id: UUID4 = Field(..., description='Айди файла')
    avatar_type: str = Field(..., description='Формат файла')
    avatar_user_id: int = Field(..., description='Айди пользователя')

    class Config:
        frozen = True
        orm_mode = True
