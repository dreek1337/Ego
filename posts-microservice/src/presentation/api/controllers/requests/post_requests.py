from src.application import (CreatePostData, DeletePostData,
                             FullTextSearchPostsData, GetPostsData,
                             UpdatePostData)


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
