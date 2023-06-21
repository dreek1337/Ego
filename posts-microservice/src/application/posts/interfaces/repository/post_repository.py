from abc import (
    ABC,
    abstractmethod
)

from src.domain import (
    PostId,
    CreatorId,
    PostAggregate
)


class PostRepo(ABC):
    """
    Репозиторий файла
    """
    @abstractmethod
    async def get_post_by_id(
            self,
            post_id: PostId
    ) -> PostAggregate:
        """Получение поста с помощью id"""

    @abstractmethod
    async def get_posts_by_creator_id(
            self,
            creator_id: CreatorId
    ) -> PostAggregate | None:
        """Получение постов с помощью id"""

    @abstractmethod
    async def create_post(self, post: PostAggregate) -> None:
        """Создание поста"""

    @abstractmethod
    async def update_post(self, post: PostAggregate) -> None:
        """Обновление поста"""

    @abstractmethod
    async def delete_post(self, post_id: PostId) -> None:
        """Удаление поста"""

    @abstractmethod
    async def like_post(self, post_id: PostId) -> None:
        """Лайк поста"""

    @abstractmethod
    async def dislike_post(self, post_id: PostId) -> None:
        """Дизлайк поста"""
