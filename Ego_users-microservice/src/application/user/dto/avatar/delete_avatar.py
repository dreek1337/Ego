from pydantic import Field

from src.application.common import DTO


class DeletedAvatarDTO(DTO):
    """Информация об удаленном файле"""
    user_id: int = Field(..., descriprion="Айди пользователя, у которого удаляем аватар")

    class Config:
        frozen = True
