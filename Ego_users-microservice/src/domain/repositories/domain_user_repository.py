from abc import (
    ABC,
    abstractmethod
)
from datetime import date
from typing import Callable

from src.domain.models import UserAggregator


class UserRepository(ABC):
    def __init__(self, session: Callable) -> None:
        self.session = session

    @abstractmethod
    def get_user(self, user_id: int) -> UserAggregator:
        """Отображает информацию профиля"""

    @abstractmethod
    def create_user(self, user: UserAggregator) -> bool:
        """Регистрация пользователя"""

    @abstractmethod
    def update_profile_info(
            self,
            *,
            user_id: int,
            username: str | None,
            email: str | None,
            gender: str | None,
            birthday: date | None
    ) -> bool:
        """Изменение данных в профиле"""

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """Делает пользователя неактивным"""
