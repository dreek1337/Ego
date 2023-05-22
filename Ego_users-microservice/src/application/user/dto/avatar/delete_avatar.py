from pydantic import (
    Field,
    UUID4
)

from src.application.common import DTO


class DeletedAvatarDTO(DTO):
    """Информация об удаленном файле"""
    avatar_id: UUID4 = Field(..., descriprion="Айди фалйа")

    class Config:
        frozen = True
