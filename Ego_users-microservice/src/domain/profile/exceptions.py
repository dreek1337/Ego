from src.domain.common import AbstractBaseException


class UserIsDeleted(AbstractBaseException):
    user_id: int

    @property
    def message(self) -> str:
        return f'The user with "{self.user_id}" id is deleted'
