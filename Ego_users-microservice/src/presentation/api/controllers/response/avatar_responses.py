from src.application import (
    AvatarDTO,
    DeletedAvatarDTO
)


class SetAvatarResponse(AvatarDTO):
    """Модель отпарвки данных об аватарке"""


class DeletedAvatarResponse(DeletedAvatarDTO):
    """Модель удаления аватарки"""
