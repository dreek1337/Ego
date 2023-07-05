from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT  # type: ignore
from src_auth.config import engine_config, pwd_config
from src_auth.infra import (
    AccessTokenManagerImpl,
    create_jwt_auth_factory,
    create_pwd_context,
    create_session_factory,
)
from src_auth.presentation.api.di import providers as prov

auth = create_jwt_auth_factory(authorize=AuthJWT)  # type: ignore
token_manager_instance = AccessTokenManagerImpl()
pool = create_session_factory(engine_config=engine_config)  # type: ignore
pwd_context = create_pwd_context(config=pwd_config)
infra_instance = prov.InfraProvider(pool=pool, pwd_context=pwd_context)


def di_builder(app: FastAPI) -> None:
    app.dependency_overrides[prov.get_uow_stub] = infra_instance.get_uow
    app.dependency_overrides[prov.get_service_stub] = prov.get_service
    app.dependency_overrides[prov.get_auth_jwt_stub] = auth
    app.dependency_overrides[
        prov.get_token_manager_stub
    ] = lambda: token_manager_instance
    app.dependency_overrides[
        prov.get_password_manager_stub
    ] = infra_instance.get_password_manager
