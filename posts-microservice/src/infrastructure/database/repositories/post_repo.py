from src.application.posts.dto import PostDTO
from src.infrastructure.database.repositories.base import PostRepoBase
from src.domain import (
    PostId,
    PostAggregate
)
from src.application.posts.interfaces import (
    PostRepo,
    PostReader,
    GetPostsFilters
)


class PostReaderImpl(PostRepoBase, PostReader):
    """
    Реализация ридера
    """
    async def get_posts_by_creator_id(
            self,
            *,
            creator_id: int,
            filters: GetPostsFilters
    ) -> list[PostDTO] | None:
        """
        Получения списка всех постов пользователя
        """
        query = {
            "query": {
                "term": {
                    "creator_id": {
                        "value": creator_id,
                    }
                }
            },
            "sort": [
                {
                    "post_date": {
                        "order": filters.order
                    }
                }
            ],
            "from": filters.offset,
            "size": filters.limit
        }

        posts = await self._connection.search(index='post-ms', body=query)

        dto_posts = self._mapper.load(from_model=posts, to_model=list[PostDTO])

        return dto_posts

    async def full_text_posts_search(
            self,
            query_string: str,
            filters: GetPostsFilters
    ) -> list[PostDTO]:
        """Полнотекстовый поиск постов"""
        query = {
            "query": {
                "match_phrase": {
                    "text_content": query_string
                }
            },
            "sort": [
                {
                    "post_date": {
                        "order": filters.order
                    }
                }
            ],
            "from": filters.offset,
            "size": filters.limit
        }

        posts = await self._connection.search(index='post-ms', body=query)

        dto_posts = self._mapper.load(from_model=posts, to_model=list[PostDTO])

        return dto_posts


class PostRepoImpl(PostRepoBase, PostRepo):
    """
    Реализация репозитория
    """
    async def get_post_by_id(
            self,
            post_id: PostId
    ) -> PostAggregate:
        """Получение поста с помощью id"""
        return None  #type: ignore

    async def create_post(self, data: PostAggregate) -> None:
        """Создание поста"""

    async def update_post(self, post: PostAggregate) -> None:
        """Обновление поста"""

    async def delete_post(self, post_id: PostId) -> None:
        """Удаление поста"""
