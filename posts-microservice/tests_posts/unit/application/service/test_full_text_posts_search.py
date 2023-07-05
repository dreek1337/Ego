import datetime

import pytest  # type: ignore
from src_posts.application import FullTextSearchPostsData, PostService
from src_posts.application.posts import dto
from src_posts.application.posts.interfaces import GetPostsOrder
from src_posts.infrastructure import MapperImpl
from tests_posts.mocks import PostUoWMock


@pytest.mark.asyncio
async def test_correct_full_text_search(uow: PostUoWMock, mapper: MapperImpl) -> None:
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
            text_content="Bad test!",
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

    uow.post_reader.add_posts(posts=posts)  # type: ignore

    data = FullTextSearchPostsData(
        query_string="My test", offset=0, limit=20, order=GetPostsOrder.ASC
    )

    full_text_search_data = await post_service.full_text_posts_search(data=data)

    correct_posts = sorted(
        [post for post in posts if data.query_string in post.text_content],
        key=lambda post: post.created_at,
    )

    assert correct_posts == full_text_search_data.posts
    assert data.offset == full_text_search_data.offset
    assert data.limit == full_text_search_data.limit


@pytest.mark.asyncio
async def test_not_found_full_text_search(uow: PostUoWMock, mapper: MapperImpl) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    posts = [
        dto.PostDTO(
            post_id="gl5MJXMBMk1dGnErnqwe",
            creator_id=0,
            text_content="Bad test!",
            created_at=datetime.datetime(
                year=2023, month=6, day=25, hour=10, minute=15
            ),
        )
    ]

    uow.post_reader.add_posts(posts=posts)  # type: ignore

    data = FullTextSearchPostsData(
        query_string="My test", offset=0, limit=20, order=GetPostsOrder.ASC
    )

    full_text_search_data = await post_service.full_text_posts_search(data=data)

    assert None is full_text_search_data.posts
    assert data.offset == full_text_search_data.offset
    assert data.limit == full_text_search_data.limit
