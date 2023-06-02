from src.application import (
    UserDTO,
    DeleteUserData
)


class UserDataResponse(UserDTO):
    """Модель получения пользоватлея"""


class DeletedUserResponse(DeleteUserData):
    """Модель данных, удаленного пользователя"""
