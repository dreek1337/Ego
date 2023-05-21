from abc import ABC

from src.application.common import UnitOfWork
from src.application.profile.interfaces import ProfileRepo


class ProfileUoW(UnitOfWork, ABC):
    def __init__(
            self,
            *,
            profile_repo: ProfileRepo
    ):
        self.profile_repo = profile_repo
