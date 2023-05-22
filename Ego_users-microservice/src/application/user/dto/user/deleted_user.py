from pydantic import Field

from src.application.common import DTO


class DeletedUserDTO(DTO):
    """
    Информация об удаленном пользователе
    """
    user_id: int = Field(..., description='Айди профиля')
    first_name: str = Field(..., description='Имя пользователя')
    last_name: str = Field(..., description='Фамилия пользователя')
    deleted: bool = Field(True, description='Указывает, что пользователь удален')

    class Config:
        frozen = True
