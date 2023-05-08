from datetime import date
from abc import ABC, abstractmethod

from src.domain.models import UserProfile


class UserRepository(ABC):
    @abstractmethod
    def get_user(
            self,
            *,
            user_id: int
    ) -> UserProfile:
        """Отображает информацию профиля"""

    @abstractmethod
    def create_user(
            self,
            *,
            username: str,
            email: str,
            password: str,
            birthday: date,
            registration_date: date,
            photo: id,
            right: str
    ) -> UserProfile:
        """Регистрация пользователя"""

    @abstractmethod
    def update_profile_info(self) -> None:
        """Изменение данных в профиле"""

    @abstractmethod
    def delete_user(
            self,
            *,
            user_id: int
    ) -> bool:
        """Делает пользователя неактивным"""
