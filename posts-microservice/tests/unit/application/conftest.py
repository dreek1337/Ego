import pytest  # type: ignore

from src.infrastructure import (
    MapperImpl,
    create_mapper
)
from tests.mocks import (
    PostUoWMock,
    PostRepoMock,
    PostReaderMock
)


@pytest.fixture
def post_repo() -> PostRepoMock:
    return PostRepoMock()


@pytest.fixture
def post_reader() -> PostReaderMock:
    return PostReaderMock()


@pytest.fixture
def uow(
        post_repo: PostRepoMock,
        post_reader: PostReaderMock
) -> PostUoWMock:
    return PostUoWMock(post_repo=post_repo, post_reader=post_reader)


@pytest.fixture
def mapper() -> MapperImpl:
    return create_mapper()
