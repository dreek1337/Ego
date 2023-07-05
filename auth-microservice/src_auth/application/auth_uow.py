from abc import ABC

from src_auth.common import UnitOfWork, UserRepo


class AuthUoW(UnitOfWork, ABC):
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo
