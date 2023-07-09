from fastapi import (
    APIRouter,
    Depends,
    status,
)
from src_posts.application import (
    PostService,
    UserIsNotPostCreator,
)
from src_posts.presentation.api.controllers import (
    requests as req,
    responses as resp,
)
from src_posts.presentation.api.di import get_service_stub

post_router = APIRouter(tags=["posts"])


@post_router.get(
    path="/posts",
    responses={status.HTTP_200_OK: {"model": resp.PostsResponse}},
    response_model=resp.PostsResponse,
)
async def get_user_posts(
    data: req.GetPostsRequest = Depends(),
    service: PostService = Depends(get_service_stub),
):
    """
    Получение всех постов пользователя
    """
    return await service.get_user_posts(data=data)


@post_router.get(
    path="/full_text_search",
    responses={status.HTTP_200_OK: {"model": resp.PostsResponse}},
    response_model=resp.PostsResponse,
)
async def full_text_posts_search(
    data: req.FullTextSearchPostsRequest = Depends(),
    service: PostService = Depends(get_service_stub),
):
    """
    Получение всех постов пользователя
    """
    return await service.full_text_posts_search(data=data)


@post_router.post(
    path="/create_post",
    responses={
        status.HTTP_201_CREATED: {"model": resp.PostResponse},
    },
    response_model=resp.PostResponse,
)
async def create_post(
    data: req.CreatePostRequest, service: PostService = Depends(get_service_stub)
):
    """
    Создание поста
    """
    return await service.create_post(data=data)


@post_router.delete(
    path="/delete_post",
    responses={
        status.HTTP_200_OK: {"model": resp.DeletedPostResponse},
        status.HTTP_403_FORBIDDEN: {"model": resp.ErrorResult[UserIsNotPostCreator]},
    },
    response_model=resp.DeletedPostResponse,
)
async def delete_post(
    data: req.DeletePostRequest, service: PostService = Depends(get_service_stub)
):
    """
    Удание поста пользователя
    """
    return await service.delete_post(data=data)


@post_router.patch(
    path="/update_post",
    responses={
        status.HTTP_200_OK: {"model": resp.PostResponse},
        status.HTTP_403_FORBIDDEN: {"model": resp.ErrorResult[UserIsNotPostCreator]},
    },
    response_model=resp.PostResponse,
)
async def update_post(
    data: req.UpdatePostRequest, service: PostService = Depends(get_service_stub)
):
    """
    Обнволение поста пользователя
    """
    return await service.update_post(data=data)
