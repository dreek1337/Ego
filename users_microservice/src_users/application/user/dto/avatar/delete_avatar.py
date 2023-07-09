from pydantic import (
    UUID4,
    Field,
)
from src_users.application.common import DTO


class DeletedAvatarDTO(DTO):
    """Информация об удаленном файле"""

    avatar_id: UUID4 = Field(..., descriprion="Айди аватара")

    class Config:
        frozen = True
        orm_mode = True
