from fastapi import FastAPI

from src.infrastructure import (
    create_mapper,
    elastic_config,
    elastic_factory
)
from src.presentation.api.di.providers import (
    get_service,
    get_uow_stub,
    get_mapper_stub,
    get_service_stub,
    InfrastructureProvider
)

engine = elastic_factory(config=elastic_config)
mapper_instance = create_mapper()
uow_instance = InfrastructureProvider(
    engine=engine,
    mapper=mapper_instance
)


def di_builder(
        app: FastAPI
) -> None:
    app.dependency_overrides[get_uow_stub] = uow_instance.get_uow
    app.dependency_overrides[get_mapper_stub] = lambda: mapper_instance
    app.dependency_overrides[get_service_stub] = get_service
