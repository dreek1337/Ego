from abc import ABC

from src.application.common import UnitOfWork
from src.application.user.interfaces import UserRepo


class UserUoW(UnitOfWork, ABC):
    def __init__(
            self,
            *,
            user_repo: UserRepo
    ):
        self.user_repo = user_repo
