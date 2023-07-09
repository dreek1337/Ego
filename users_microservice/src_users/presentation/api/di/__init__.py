from fastapi import FastAPI
from src_users.infrastructure import (
    cloud_config,
    engine_config,
    s3_factory,
)
from src_users.infrastructure.database.main import create_session_factory
from src_users.infrastructure.mapper.main import create_mapper
from src_users.presentation.api.di.providers import (
    InfrastructureProvider,
    get_cloud_storage_stub,
    get_mapper_stub,
    get_service,
    get_service_stub,
    get_uow_stub,
)

mapper_instance = create_mapper()
minio_connection = s3_factory(cloud_config=cloud_config)
pool = create_session_factory(engine_config=engine_config)
infra_instance = InfrastructureProvider(
    pool=pool, mapper=mapper_instance, cloud_connection=minio_connection
)


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[get_uow_stub] = infra_instance.get_uow
    app.dependency_overrides[get_mapper_stub] = lambda: mapper_instance
    app.dependency_overrides[get_cloud_storage_stub] = infra_instance.get_cloud_storage
    app.dependency_overrides[get_service_stub] = get_service
