from datetime import date
from abc import ABC, abstractmethod

from src.domain.models import (
    UserProfile,
    UserRegistrationInfo
)


class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> UserProfile:
        """Отображает информацию профиля"""

    @abstractmethod
    def create_user(
            self,
            *,
            username: str,
            email: str,
            password: str,
            gender: str | None = None,
            birthday: date | None = None
    ) -> UserRegistrationInfo:
        """Регистрация пользователя"""

    @abstractmethod
    def update_profile_info(
            self,
            *,
            user_id: int,
            username: str | None = None,
            email: str | None = None,
            gender: str | None = None,
            birthday: date | None = None,
    ) -> bool:
        """Изменение данных в профиле"""

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """Делает пользователя неактивным"""
