from datetime import date

from src.domain.common import (
    UserProfile,
    UserRegistrationInfo
)
from src.application.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_user_info(self, user_id: int) -> UserProfile:
        """
        Получаем данные профиля пользователя по id или по username
        """
        return self.user_repository.get_user(user_id=user_id)

    def registration_user(
            self,
            *,
            username: str,
            email: str,
            password: str,
            gender: str | None = None,
            birthday: date | None = None,
    ) -> UserRegistrationInfo:
        """
        Регистрация пользователя
        """
        return self.user_repository.create_user(
            username=username,
            email=email,
            password=password,
            gender=gender,
            birthday=birthday
        )

    def update_user_data(
            self,
            *,
            user_id: int,
            email: str | None = None,
            gender: str | None = None,
            birthday: date | None = None
    ) -> bool:
        """
        Обновление данных профиля
        """
        return self.user_repository.update_profile_info(
            user_id=user_id,
            email=email,
            gender=gender,
            birthday=birthday
        )

    def delete_user(self, user_id: int) -> bool:
        """
        Удаление пользователя
        """
        return self.user_repository.delete_user(user_id=user_id)
