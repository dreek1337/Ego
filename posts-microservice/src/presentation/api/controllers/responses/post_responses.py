from src.application.posts.dto import DeletePostDTO, PostDTO, PostsDTO


class PostResponse(PostDTO):
    """Модель ответа для получения поста"""


class PostsResponse(PostsDTO):
    """Модель ответа для получения постов"""


class DeletedPostResponse(DeletePostDTO):
    """Модель овтета при удалении поста"""
