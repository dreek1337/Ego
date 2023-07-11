from pydantic import BaseModel
from src_posts.application.posts.interfaces import GetPostsOrder
from src_posts.domain import Empty


class GetPostsRequest(BaseModel):
    """
    Модель запрсоа для полученяи постов
    """

    creator_id: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC


class FullTextSearchPostsRequest(BaseModel):
    """
    Модель запрсоа для полученяи постов по тексту
    """

    query_string: str
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC


class CreatePostRequest(BaseModel):
    """
    Модель для создания поста
    """

    text_content: str


class DeletePostRequest(BaseModel):
    """
    Модель для удаления поста
    """

    post_id: str


class UpdatePostRequest(BaseModel):
    """
    Модель для обнавления поста
    """

    post_id: str
    text_content: str
