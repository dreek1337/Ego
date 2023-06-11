from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from src.config import EngineConfig


def create_sa_session(
        engine_config: EngineConfig
) -> async_sessionmaker[AsyncSession]:
    """
    Создание асинхронной сессии
    """
    engine = create_async_engine(**engine_config.dict())

    session_factory = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )

    return session_factory
