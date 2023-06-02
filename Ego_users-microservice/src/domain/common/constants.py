from enum import Enum


class Empty(str, Enum):
    UNSET = "UNSET"


class ValidAvatarType(str, Enum):
    JPEG = 'jpeg'
    JPG = 'jpg'
    PNG = 'png'


class GenderValue(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
