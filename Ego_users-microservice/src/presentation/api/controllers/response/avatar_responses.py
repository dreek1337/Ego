from pydantic import validator

from src.application import SetAvatarData, DeletedAvatarDTO


class SetAvatarResponse(SetAvatarData):
    """Модель отпарвки данных об аватарке"""
    @validator('avatar_content')
    def dump_avatar_content(cls, value):
        if value:
            return str(value)


class DeletedAvatarResponse(DeletedAvatarDTO):
    """Модель удаления аватарки"""
