from fastapi import FastAPI

from src.infrastructure.database.main import create_session_factory
from src.infrastructure.mapper.main import create_mapper
from src.presentation.api.di.providers.stubs import get_mapper_stub, get_session_stub


def setup_di(
        app: FastAPI
) -> None:
    app.dependency_overrides[get_mapper_stub] = create_mapper
    app.dependency_overrides[get_session_stub] = create_session_factory
