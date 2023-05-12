from src.domain.common import AbstractBaseException
from dataclasses import dataclass


@dataclass
class UserIsDeleted(AbstractBaseException):
    user_id: int

    @property
    def message(self) -> str:
        return f'The user with "{self.user_id}" id is deleted'
