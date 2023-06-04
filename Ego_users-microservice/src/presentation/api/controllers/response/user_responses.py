from pydantic import validator

from src.application import (
    UserDTO,
    DeleteUserData
)


class UserDataResponse(UserDTO):
    """Модель получения пользоватлея"""

    @validator('avatar')
    def dump_avatar_content(cls, value):
        if value:
            return str(value.avatar_content)


class DeletedUserResponse(DeleteUserData):
    """Модель данных, удаленного пользователя"""
