from abc import ABC

from src.common import (
    UnitOfWork,
    RepositoryBase
)


class AuthUoW(UnitOfWork, ABC):
    def __init__(self, user_repo: RepositoryBase):
        self.user_repo = user_repo
