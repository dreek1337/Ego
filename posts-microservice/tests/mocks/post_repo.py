import datetime

from elasticsearch.exceptions import NotFoundError  # type: ignore
from src.application.posts.interfaces import PostRepo
from src.domain import PostAggregate, PostId


class PostRepoMock(PostRepo):
    """
    Репозиторий постов
    """
    def __init__(self) -> None:
        self.posts: dict[PostId, PostAggregate] = dict()

    async def get_post_by_id(self, post_id: PostId) -> PostAggregate:
        """
        Получение поста с помощью id
        """
        if post_id not in self.posts:
            raise NotFoundError()

        return self.posts[post_id]

    async def create_post(self, data: PostAggregate) -> PostAggregate:
        """
        Создание поста
        """
        post_id = PostId(value="gl5MJXMBMk1dGnErnBW8")
        created_at = datetime.datetime(
            year=2023,
            month=6,
            day=25,
            hour=11,
            minute=15
        )
        data.post_id = post_id
        data.created_at = created_at

        self.posts[post_id] = data

        return data

    async def update_post(self, post: PostAggregate) -> None:
        """
        Обновление поста
        """
        self.posts[post.post_id] = post  # type: ignore

    async def delete_post(self, post_id: PostId) -> None:
        """
        Удаление поста
        """
        if post_id not in self.posts:
            raise NotFoundError()

        del self.posts[post_id]

    def add_post(self, post: PostAggregate) -> None:
        """
        Добавление поста для тестирования
        """
        self.posts[post.post_id] = post  # type: ignore
