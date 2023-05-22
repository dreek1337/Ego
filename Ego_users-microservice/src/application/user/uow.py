from abc import ABC

from src.application.common import UnitOfWork
from src.application.user.interfaces import (
    UserRepo,
    AvatarRepo,
    SubscriptionRepo
)


class UserUoW(UnitOfWork, ABC):
    def __init__(
            self,
            *,
            user_repo: UserRepo,
            avatar_repo: AvatarRepo,
            subscription_repo: SubscriptionRepo
    ):
        self.user_repo = user_repo
        self.avatar_repo = avatar_repo
        self.subscription_repo = subscription_repo
