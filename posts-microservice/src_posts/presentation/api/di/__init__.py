from fastapi import FastAPI
from src_posts.infrastructure import create_mapper, elastic_config, elastic_factory
from src_posts.presentation.api.di.providers import (
    InfrastructureProvider,
    get_mapper_stub,
    get_service,
    get_service_stub,
    get_uow_stub,
)

engine = elastic_factory(config=elastic_config)
mapper_instance = create_mapper()
uow_instance = InfrastructureProvider(engine=engine, mapper=mapper_instance)


def di_builder(app: FastAPI) -> None:
    app.dependency_overrides[get_uow_stub] = uow_instance.get_uow
    app.dependency_overrides[get_mapper_stub] = lambda: mapper_instance
    app.dependency_overrides[get_service_stub] = get_service
