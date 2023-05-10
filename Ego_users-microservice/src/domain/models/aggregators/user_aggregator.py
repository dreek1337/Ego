from dataclasses import dataclass

from src.domain.models.entities import (
    FileInfo,
    Post,
    Subscription,
    Subscriber
)
from src.domain.models.value_objects import (
    UserId,
    UserName,
    UserEmail,
    UserRights,
    UserGender,
    UserActive,
    UserBirthday,
    UserPassword,
    UserRegistrationDate
)


@dataclass
class User:
    """
    Полная модель пользователя
    """
    user_id: UserId
    username: UserName
    email: UserEmail
    password: UserPassword
    gender: UserGender
    birthday: UserBirthday
    registration_date: UserRegistrationDate
    is_active: UserActive
    rights: UserRights
    photo: FileInfo
    posts: list[Post]
    subscriptions: list[Subscription]
    subscribers: list[Subscriber]
