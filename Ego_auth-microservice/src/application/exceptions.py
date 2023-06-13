from dataclasses import dataclass

from src.common import BaseAppException


@dataclass
class UserDataIsNotCorrect(BaseAppException):
    def message(self) -> str:
        return 'Username or password is not correct!'
