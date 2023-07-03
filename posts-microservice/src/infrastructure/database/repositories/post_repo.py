from src.application.posts.dto import PostDTO
from src.infrastructure.database.repositories.base import ElasticPostRepoBase
from src.domain import (
    PostId,
    PostAggregate, Empty
)
from src.application.posts.interfaces import (
    PostRepo,
    PostReader,
    GetPostsFilters
)
from src.application import ElasticIndexes


class PostReaderImpl(ElasticPostRepoBase, PostReader):
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
                    "created_at": {
                        "order": filters.order
                    }
                }
            ]
        }

        if filters.offset != Empty.UNSET.value:
            query["from"] = filters.offset  # type: ignore
        if filters.limit != Empty.UNSET.value:
            query["size"] = filters.limit  # type: ignore

        async with self._engine() as connection:
            posts = await connection.search(
                index=ElasticIndexes.POST_MS.value,
                body=query
            )

        list_of_posts = posts.get('hits').get('hits')

        if not list_of_posts:
            return None

        dto_posts = self._mapper.load(from_model=list_of_posts, to_model=list[PostDTO])

        return dto_posts

    async def full_text_posts_search(
            self,
            query_string: str,
            filters: GetPostsFilters
    ) -> list[PostDTO] | None:
        """
        Полнотекстовый поиск постов
        """
        query = {
            "query": {
                "match_phrase": {
                    "text_content": query_string
                }
            },
            "sort": [
                {
                    "created_at": {
                        "order": filters.order
                    }
                }
            ]
        }

        if filters.offset != Empty.UNSET.value:
            query["from"] = filters.offset  # type: ignore
        if filters.limit != Empty.UNSET.value:
            query["size"] = filters.limit  # type: ignore

        async with self._engine() as connection:
            posts = await connection.search(
                index=ElasticIndexes.POST_MS.value,
                body=query
            )

        list_of_posts = posts.get('hits').get('hits')

        if not list_of_posts:
            return None

        dto_posts = self._mapper.load(from_model=list_of_posts, to_model=list[PostDTO])

        return dto_posts


class PostRepoImpl(ElasticPostRepoBase, PostRepo):
    """
    Реализация репозитория
    """
    async def get_post_by_id(
            self,
            post_id: PostId
    ) -> PostAggregate:
        """
        Получение поста с помощью id
        """
        async with self._engine() as connection:
            post = await connection.get(
                index=ElasticIndexes.POST_MS.value,
                id=post_id.get_value
            )

        post_aggregate = self._mapper.load(from_model=post, to_model=PostAggregate)

        return post_aggregate

    async def create_post(self, data: PostAggregate) -> PostAggregate:
        """
        Создание поста
        """
        document = {
            'creator_id': data.creator_id.get_value,
            'text_content': data.text_content,
            'created_at': data.created_at
        }
        async with self._engine() as connection:
            created_data = await connection.index(
                index=ElasticIndexes.POST_MS.value,
                document=document
            )

        data.post_id = PostId(value=created_data.get('_id'))

        return data

    async def update_post(self, post: PostAggregate) -> None:
        """
        Обновление поста
        """
        document = {
            "doc": {
                'text_content': post.text_content,
            }
        }
        async with self._engine() as connection:
            await connection.update(
                index=ElasticIndexes.POST_MS.value,
                id=post.post_id.get_value,  # type: ignore
                body=document
            )

    async def delete_post(self, post_id: PostId) -> None:
        """
        Удаление поста
        """
        async with self._engine() as connection:
            await connection.delete(
                index=ElasticIndexes.POST_MS.value,
                id=post_id.get_value
            )
