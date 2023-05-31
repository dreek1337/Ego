from fastapi import FastAPI

from src.presentation.api.controllers.healthcheck_router import health_check_router


def setup_controllers(
        app: FastAPI
) -> None:
    app.include_router(health_check_router)

