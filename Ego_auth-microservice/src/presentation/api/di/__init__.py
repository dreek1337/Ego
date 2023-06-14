from fastapi import FastAPI

from src.presentation.api.di import providers as prov
from src.config import (
    pwd_config,
    jwt_config,
    engine_config
)
from src.infra import (
    get_jwt_auth,
    create_pwd_context,
    create_session_factory,
    AccessTokenManagerImpl
)

token_manager_instance = AccessTokenManagerImpl()
jwt_auth_instance = get_jwt_auth(config=jwt_config)
pool = create_session_factory(engine_config=engine_config)  # type: ignore
pwd_context = create_pwd_context(config=pwd_config)
infra_instance = prov.InfraProvider(
    pool=pool,
    pwd_context=pwd_context
)


def di_builder(
        app: FastAPI
) -> None:
    app.dependency_overrides[prov.get_uow_stub] = infra_instance.get_uow
    app.dependency_overrides[prov.get_service_stub] = prov.get_service
    app.dependency_overrides[prov.get_auth_jwt_stub] = lambda: jwt_auth_instance
    app.dependency_overrides[prov.get_token_manager_stub] = lambda: token_manager_instance
    app.dependency_overrides[prov.get_password_manager_stub] = infra_instance.get_password_manager
