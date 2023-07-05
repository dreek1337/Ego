import datetime

import pytest  # type: ignore
from src_posts.application import GetPostsData, PostService
from src_posts.application.posts import dto
from src_posts.application.posts.interfaces import GetPostsOrder
from src_posts.infrastructure import MapperImpl
from tests_posts.mocks import PostUoWMock


@pytest.mark.asyncio
async def test_get_user_posts(uow: PostUoWMock, mapper: MapperImpl) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    posts = [
        dto.PostDTO(
            post_id="gl5MJXMBMk1dGnErnBW8",
            creator_id=0,
            text_content="My test post!",
            created_at=datetime.datetime(
                year=2023, month=6, day=25, hour=11, minute=15
            ),
        ),
        dto.PostDTO(
            post_id="gl5MJXMBMk1dGnErnqwe",
            creator_id=0,
            text_content="My test post!",
            created_at=datetime.datetime(
                year=2023, month=6, day=25, hour=10, minute=15
            ),
        ),
        dto.PostDTO(
            post_id="gl5MJXMBMk1dGnErLLLL",
            creator_id=1,
            text_content="My test post!",
            created_at=datetime.datetime(
                year=2023, month=6, day=25, hour=10, minute=15
            ),
        ),
    ]

    uow.post_reader.add_posts(posts)  # type: ignore

    data = GetPostsData(creator_id=0, offset=0, limit=20, order=GetPostsOrder.DESC)

    user_posts = await post_service.get_user_posts(data=data)

    correct_posts = sorted(
        [post for post in posts if post.creator_id == 0],
        key=lambda post: post.created_at,
        reverse=True,
    )

    assert correct_posts == user_posts.posts
    assert data.offset == user_posts.offset
    assert data.limit == user_posts.limit


@pytest.mark.asyncio
async def test_get_user_posts_empty(uow: PostUoWMock, mapper: MapperImpl) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    posts = [
        dto.PostDTO(
            post_id="gl5MJXMBMk1dGnErLLLL",
            creator_id=1,
            text_content="My test post!",
            created_at=datetime.datetime(
                year=2023, month=6, day=25, hour=10, minute=15
            ),
        )
    ]

    uow.post_reader.add_posts(posts)  # type: ignore

    data = GetPostsData(creator_id=0, offset=0, limit=20, order=GetPostsOrder.DESC)

    user_posts = await post_service.get_user_posts(data=data)

    assert None is user_posts.posts
    assert data.offset == user_posts.offset
    assert data.limit == user_posts.limit
