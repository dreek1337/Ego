from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def get_profile(self) -> UserProfile:
        """Отображает информацию профиля"""

    @abstractmethod
    def registration(self) -> UserRegistration:
        """Регистрация пользователя"""

    @abstractmethod
    def update_info(self) -> None:
        """Изменение данных в профиле"""

    @abstractmethod
    def delete_user(self) -> None:
        """Делает пользователя неактивным"""
