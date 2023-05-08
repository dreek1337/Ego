from abc import ABC, abstractmethod

from src.domain.models import Profile


class ProfileRepository(ABC):
    @abstractmethod
    def get_profile_info(self) -> Profile:
        """Получение информации о профиле"""
