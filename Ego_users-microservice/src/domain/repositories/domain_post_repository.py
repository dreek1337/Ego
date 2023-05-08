from abc import ABC, abstractmethod

from src.domain.models import Post


class PostRepository(ABC):
    @abstractmethod
    def get_user_posts(self) -> list[Post]:
        """Получение всех постов пользователя"""
