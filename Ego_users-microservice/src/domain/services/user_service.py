from datetime import date

from src.domain.models import UserProfile
from src.domain.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_profile(
            self,
            *,
            user_id: int
    ) -> UserProfile:
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
            birthday: date,
            registration_date: date,
            photo: id,
            right: str
    ) -> UserProfile:
        """
        Регистрация пользователя
        """
        return self.user_repository.create_user(
            username=username,
            email=email,
            password=password,
            birthday=birthday,
            registration_date=registration_date,
            photo=photo,
            right=right
        )

    def change_profile_data(
            self,
            *,
            user_id
    ) -> bool:
        """
        Обновление данных профиля
        """

    def change_email(
            self,
            *,
            user_id,
            new_email
    ) -> bool:
        pass
