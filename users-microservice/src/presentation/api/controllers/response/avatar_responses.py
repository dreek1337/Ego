from src.application import (
    AvatarDTO,
    DeletedAvatarDTO
)


class SetAvatarResponse(AvatarDTO):
    """Модель ответа отпарвки данных об аватарке"""


class DeletedAvatarResponse(DeletedAvatarDTO):
    """Модель ответа удаления аватарки"""
