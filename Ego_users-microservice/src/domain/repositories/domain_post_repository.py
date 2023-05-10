from abc import ABC, abstractmethod

from src.domain.models import Post


class PostRepository(ABC):
    @abstractmethod
    def get_user_posts(self, user_id: int) -> list[Post]:
        """Получение всех постов пользователя"""
