from src.application import (
    UserDTO,
    DeleteUserData
)


class UserDataResponse(UserDTO):
    """Модель ответа получения пользоватлея"""


class DeletedUserResponse(DeleteUserData):
    """Модель ответа данных, удаленного пользователя"""
