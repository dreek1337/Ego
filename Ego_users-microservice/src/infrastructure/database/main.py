from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from src.infrastructure.database.config import EngineConfig


async def create_engine(
        engine_config: EngineConfig
) -> AsyncGenerator[AsyncEngine, None]:
    """
    Создание engine с настройками
    """
    engine = create_async_engine(**engine_config.dict())

    yield engine

    await engine.dispose()


def create_session_factory(
        engine: AsyncEngine
) -> async_sessionmaker[AsyncSession]:
    """
    Создание сессии с настройками
    """
    session_factory = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )

    return session_factory


async def create_session(
        session_factory: async_sessionmaker[AsyncSession]
) -> AsyncGenerator[AsyncSession, None]:
    """
    Получение сессии для работы с бд
    """
    async with session_factory() as session:
        yield session
