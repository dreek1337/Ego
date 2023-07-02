import pytest  # type: ignore

from tests.mocks import (
    PostRepoMock,
    PostReaderMock
)


@pytest.fixture
def post_repo() -> PostRepoMock:
    return PostRepoMock()


@pytest.fixture
def post_reader() -> PostReaderMock:
    return PostReaderMock()
