from abc import (
    ABC,
    abstractmethod,
)

from src_posts.domain import (
    PostAggregate,
    PostId,
)


class PostRepo(ABC):
    """
    Репозиторий постов
    """

    @abstractmethod
    async def get_post_by_id(self, post_id: PostId) -> PostAggregate:
        """Получение поста с помощью id"""

    @abstractmethod
    async def create_post(self, data: PostAggregate) -> PostAggregate:
        """Создание поста"""

    @abstractmethod
    async def update_post(self, post: PostAggregate) -> None:
        """Обновление поста"""

    @abstractmethod
    async def delete_post(self, post_id: PostId) -> None:
        """Удаление поста"""
