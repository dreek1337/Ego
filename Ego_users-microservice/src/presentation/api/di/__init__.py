from fastapi import FastAPI

from src.infrastructure import engine_config
from src.infrastructure.mapper.main import create_mapper
from src.infrastructure.database.main import create_session_factory
from src.presentation.api.di.providers import (
    UoWProvider,
    get_service
)
from src.presentation.api.di.providers import (
    get_uow_stub,
    get_mapper_stub,
    get_service_stub
)

pool = create_session_factory(engine_config=engine_config)
mapper_instance = create_mapper()
uow_instance = UoWProvider(pool=pool, mapper=mapper_instance)


def setup_di(
        app: FastAPI
) -> None:
    app.dependency_overrides[get_uow_stub] = uow_instance.get_uow
    app.dependency_overrides[get_mapper_stub] = lambda: mapper_instance
    app.dependency_overrides[get_service_stub] = get_service
