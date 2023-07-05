from src_posts.application.posts import dto
from src_posts.application.posts.interfaces import (
    GetPostsFilters,
    GetPostsOrder,
    PostReader,
)
from src_posts.domain import Empty


class PostReaderMock(PostReader):
    """
    Ридер для работы с бд
    """

    def __init__(self) -> None:
        self.posts: dict[str, dto.PostDTO] = dict()

    async def get_posts_by_creator_id(
        self, *, creator_id: int, filters: GetPostsFilters
    ) -> list[dto.PostDTO] | None:
        """
        Получения списка всех постов пользователя
        """
        posts = [post for post in self.posts.values() if post.creator_id == creator_id]

        if not posts:
            return None

        posts = self._add_filters(posts=posts, filters=filters)

        return posts

    async def full_text_posts_search(
        self, query_string: str, filters: GetPostsFilters
    ) -> list[dto.PostDTO] | None:
        """
        Полнотекстовый поиск постов
        """
        posts = [
            post for post in self.posts.values() if query_string in post.text_content
        ]

        if not posts:
            return None

        posts = self._add_filters(posts=posts, filters=filters)

        return posts

    def add_post(self, post: dto.PostDTO) -> None:
        """
        Добавление поста для тестирования
        """
        self.posts[post.post_id] = post

    def add_posts(self, posts: list[dto.PostDTO]) -> None:
        """
        Добавление постов для тестирования
        """
        for post in posts:
            self.add_post(post=post)

    @staticmethod
    def _add_filters(
        posts: list[dto.PostDTO], filters: GetPostsFilters
    ) -> list[dto.PostDTO]:
        """
        Добавление фильтров
        """
        if filters.order == GetPostsOrder.ASC:
            posts.sort(key=lambda post: post.created_at)
        else:
            posts.sort(key=lambda post: post.created_at, reverse=True)

        limit = filters.limit if filters.limit is not Empty.UNSET else 0
        offset = filters.offset if filters.offset is not Empty.UNSET else len(posts)
        last_index = limit + offset

        posts = posts[offset:last_index]

        return posts
