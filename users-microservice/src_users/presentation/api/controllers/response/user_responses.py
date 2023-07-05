from src_users.application import DeleteUserData, UserDTO


class UserDataResponse(UserDTO):
    """Модель ответа получения пользоватлея"""


class DeletedUserResponse(DeleteUserData):
    """Модель ответа данных, удаленного пользователя"""
