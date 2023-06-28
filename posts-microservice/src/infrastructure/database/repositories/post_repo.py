from src.application import ElasticIndexes
from src.application.posts.dto import PostDTO
from src.infrastructure.database.repositories.base import PostRepoBase
from src.infrastructure.database.error_interceptor import error_interceptor
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
    @error_interceptor
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
                    "creator_id": {
                        "order": filters.order
                    }
                }
            ],
            "from": filters.offset,
            "size": filters.limit
        }

        posts = await self._connection.search(
            index=ElasticIndexes.POST_MS.value,
            body=query
        )
        print()
        list_of_posts = posts.get('hits').get('hits')

        if list_of_posts:
            return None

        dto_posts = self._mapper.load(from_model=list_of_posts, to_model=list[PostDTO])

        return dto_posts

    @error_interceptor
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
                    "creator_id": {
                        "order": filters.order
                    }
                }
            ],
            "from": filters.offset,
            "size": filters.limit
        }

        posts = await self._connection.search(
            index=ElasticIndexes.POST_MS.value,
            body=query
        )

        list_of_posts = posts.get('hits').get('hits')

        if list_of_posts:
            return None

        dto_posts = self._mapper.load(from_model=list_of_posts, to_model=list[PostDTO])

        return dto_posts


class PostRepoImpl(PostRepoBase, PostRepo):
    """
    Реализация репозитория
    """

    @error_interceptor
    async def get_post_by_id(
            self,
            post_id: PostId
    ) -> PostAggregate:
        """
        Получение поста с помощью id
        """
        post = await self._connection.get(
            index=ElasticIndexes.POST_MS.value,
            id=post_id.get_value
        )

        post_aggregate = self._mapper.load(from_model=post, to_model=PostAggregate)

        return post_aggregate

    @error_interceptor
    async def create_post(self, data: PostAggregate) -> PostAggregate:
        """
        Создание поста
        """
        document = {
            'creator_id': data.creator_id.get_value,
            'text_content': data.text_content,
            'created_at': data.created_at
        }

        created_data = await self._connection.index(
            index=ElasticIndexes.POST_MS.value,
            document=document
        )

        if created_data.get('result') != 'created':
            raise Exception

        data.post_id = created_data.get('_id')

        return data

    @error_interceptor
    async def update_post(self, post: PostAggregate) -> PostAggregate:
        """
        Обновление поста
        """
        document = {
            "doc": {
                'text_content': post.text_content,
            }
        }

        updated_data = await self._connection.update(
            index=ElasticIndexes.POST_MS.value,
            id=post.post_id.get_value,  # type: ignore
            body=document
        )

        if not updated_data.get('found'):
            raise Exception

        post.post_id = updated_data.get('_id')

        return post

    @error_interceptor
    async def delete_post(self, post_id: PostId) -> None:
        """
        Удаление поста
        """
        deleted_data = await self._connection.delete(
            index=ElasticIndexes.POST_MS.value,
            id=post_id.get_value
        )

        if deleted_data.get('result') != 'deleted':
            raise Exception
