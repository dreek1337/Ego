from src.application import (
    GetPostsData,
    CreatePostData,
    DeletePostData,
    UpdatePostData,
    FullTextSearchPostsData
)


class GetPostsRequest(GetPostsData):
    """Модель запрсоа для полученяи постов"""


class FullTextSearchPostsRequest(FullTextSearchPostsData):
    """Модель запрсоа для полученяи постов по тексту"""


class CreatePostRequest(CreatePostData):
    """Модель для создания поста"""


class DeletePostRequest(DeletePostData):
    """Модель для удаления поста"""


class UpdatePostRequest(UpdatePostData):
    """Модель для обнавления поста"""
