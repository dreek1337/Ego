from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src_auth.config import EngineConfig


def create_session_factory(
    engine_config: EngineConfig,
) -> async_sessionmaker[AsyncSession]:
    """
    Создание асинхронной сессии
    """
    engine = create_async_engine(**engine_config.dict())

    session_factory = async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False
    )

    return session_factory


async def create_sa_session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncGenerator[AsyncSession, None]:
    """
    Получение сессии для работы с бд
    """
    async with session_factory() as session:
        yield session
