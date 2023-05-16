from abc import (
    ABC,
    abstractmethod
)

from src.domain import FileEntity


class PostsRepo(ABC):
    """
    Репозиторий постов
    """
    @abstractmethod
    async def get_posts_by_profile_id(self, profile_id: int) -> FileEntity:
        """Получение постов с помощью id пользователя"""
